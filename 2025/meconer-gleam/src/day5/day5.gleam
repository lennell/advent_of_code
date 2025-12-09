import gleam/int
import gleam/io
import gleam/list
import gleam/result
import gleam/string
import utils

pub fn get_input(path) {
  let input = utils.read_input(path) |> string.split("\n\n")
  case input {
    [a, b] -> {
      #(a, b)
    }

    _ -> {
      #("", "")
    }
  }
}

pub fn is_fresh(ingr: Int, ranges: List(#(Int, Int))) -> Bool {
  list.any(ranges, fn(range) {
    let #(first, last) = range
    ingr >= first && ingr <= last
  })
}

pub fn parse_ranges(ranges_str: String) -> List(#(Int, Int)) {
  string.split(ranges_str, "\n")
  |> list.map(fn(line) {
    string.split(line, on: "-")
    |> list.map(fn(s) { int.parse(s) |> result.unwrap(0) })
  })
  |> list.map(fn(rl) {
    case rl {
      [a, b] -> #(a, b)
      _ -> panic as "Err"
    }
  })
}

pub fn day5p1(path) -> Int {
  let #(ranges, ingredients) = get_input(path)
  let ranges = parse_ranges(ranges)
  let ingredients =
    string.split(ingredients, "\n")
    |> list.map(fn(s) { int.parse(s) |> result.unwrap(0) })
  let fresh_ingredients =
    list.filter(ingredients, fn(ing) { is_fresh(ing, ranges) })
  let res = list.length(fresh_ingredients)

  io.println("Day 5 part 1 : " <> int.to_string(res))
  res
}

pub fn combine_ranges(r1: #(Int, Int), r2: #(Int, Int)) -> List(#(Int, Int)) {
  let #(r1s, r1e) = r1
  let #(r2s, r2e) = r2

  case r1s < r2s {
    True ->
      case r1e < r2s {
        True -> [r1, r2]
        False -> [#(r1s, int.max(r1e, r2e))]
      }
    False ->
      case r1s == r2s {
        True -> [#(r1s, int.max(r1e, r2e))]
        False -> {
          // r2 starts before r1
          case r2e < r1s {
            True -> [r2, r1]
            False -> [#(r2s, int.max(r1e, r2e))]
          }
        }
      }
  }
}

// Checks if two ranges overlaps
pub fn overlaps(r1: #(Int, Int), r2: #(Int, Int)) -> Bool {
  let #(r1s, r1e) = r1
  let #(r2s, r2e) = r2
  case r1s < r2s {
    True -> r1e >= r2s
    False -> r2e >= r1s
  }
}

pub fn build_non_overlapping_ranges(
  range_list: List(#(Int, Int)),
) -> List(#(Int, Int)) {
  list.fold(range_list, [], fn(acc_non_overlapping, range) {
    case acc_non_overlapping {
      [] -> [range]
      // First range. 
      [a_range] -> {
        // Only 1 range accumulated
        let combined = combine_ranges(a_range, range)
        combined
      }
      acc_n_o -> {
        // Multiple ranges collected
        // Only consider the ones that are overlapping with the new one
        let #(overlapping, non_overlapping) =
          list.partition(acc_n_o, fn(rng) { overlaps(range, rng) })
        // Combine the overlapping ranges into a single range. Since
        // they all are overlapping the new one, they all should combine
        // to only one
        let new_range =
          list.fold(overlapping, range, fn(acc_range, rng) {
            let combined = combine_ranges(acc_range, rng)
            case combined {
              [cr] -> cr
              _ ->
                panic as "The overlapping ranges should combine to only one range"
            }
          })
        [new_range, ..non_overlapping]
        // Add the new range to the list.
      }
    }
  })
}

pub fn day5p2(path: String) -> Int {
  let #(ranges, _ingredients) = get_input(path)
  let ranges = parse_ranges(ranges)
  let non_overlapping_ranges = build_non_overlapping_ranges(ranges)

  let res =
    list.fold(non_overlapping_ranges, 0, fn(acc, range) {
      let #(rs, re) = range
      acc + re - rs + 1
    })
  io.println("Day 5 part 2 : " <> int.to_string(res))
  res
}
