import gleam/int
import gleam/io
import gleam/list
import gleam/string
import utils

fn is_valid(n: Int) -> Bool {
  let s = int.to_string(n)
  let mid = string.length(s) / 2
  let first_half = string.slice(s, 0, mid)
  let second_half = string.slice(s, mid, string.length(s))
  first_half != second_half
}

pub fn is_valid_p2_inner(s1, s2, chunk_size) {
  case string.starts_with(s2, s1) {
    True -> {
      let new_rest = string.drop_start(s2, chunk_size)
      case string.length(new_rest) == 0 {
        True -> False
        False -> is_valid_p2_inner(s1, new_rest, chunk_size)
      }
    }
    False -> True
  }
}

fn is_valid_p2_rec(s: String, chunk_size: Int) -> Bool {
  let first_chunk = string.slice(s, 0, chunk_size)
  let rest = string.drop_start(s, chunk_size)
  let is_valid = case string.length(rest) {
    n if n == 0 -> True
    n if n < chunk_size -> True
    _ -> is_valid_p2_inner(first_chunk, rest, chunk_size)
  }
  case is_valid {
    True -> {
      // Still not invalid. Check next longer chunk_size
      let half = string.length(s) / 2
      let new_chunk_size = chunk_size + 1
      case new_chunk_size {
        cs if cs > half -> True
        cs -> is_valid_p2_rec(s, cs)
      }
    }
    False -> False
  }
}

pub fn is_valid_p2(n: Int) -> Bool {
  let s = int.to_string(n)
  is_valid_p2_rec(s, 1)
}

fn get_input(path) {
  utils.read_input(path)
  |> string.split(on: ",")
  |> list.map(fn(line) {
    string.split(line, on: "-")
    |> list.map(utils.safe_int_parse)
  })
  |> list.map(fn(list) {
    case list {
      [a, b] -> #(a, b)
      _ -> panic as "Err"
    }
  })
}

pub fn day2p1(path) -> Int {
  let input = get_input(path)
  let invalids =
    input
    |> list.fold([], fn(acc, tup) {
      let range = list.range(tup.0, tup.1)
      let inv =
        list.fold(range, [], fn(acc2, n) {
          case is_valid(n) {
            False -> [n, ..acc2]
            True -> acc2
          }
        })
      list.append(inv, acc)
    })
  let sum = list.fold(invalids, 0, fn(acc, n) { acc + n })
  io.println("Day 2, Part 1 : " <> int.to_string(sum))
  sum
}

pub fn day2p2(path) -> Int {
  let input = get_input(path)
  let invalids =
    input
    |> list.fold([], fn(acc, tup) {
      let range = list.range(tup.0, tup.1)
      let inv =
        list.fold(range, [], fn(acc2, n) {
          case is_valid_p2(n) {
            False -> [n, ..acc2]
            True -> acc2
          }
        })
      list.append(inv, acc)
    })
  let sum = list.fold(invalids, 0, fn(acc, n) { acc + n })
  io.println("Day 2, Part 1 : " <> int.to_string(sum))
  sum
}
