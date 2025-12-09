import gleam/dict
import gleam/int
import gleam/io
import gleam/list
import gleam/result
import gleam/set
import gleam/string
import utils

fn find_splitters(line: String) -> set.Set(Int) {
  line
  |> string.to_graphemes
  |> list.index_fold(set.new(), fn(acc, gr, idx) {
    case gr {
      "^" -> set.insert(acc, idx)
      _ -> acc
    }
  })
}

fn split_beams(
  beams: set.Set(Int),
  lines: List(String),
  count: Int,
) -> #(Int, set.Set(Int)) {
  case lines {
    [] -> #(count, beams)
    [first_line, ..rest] -> {
      let splitters = find_splitters(first_line)
      let #(new_count, new_beams) =
        set.fold(beams, #(count, set.new()), fn(acc, beam) {
          let #(count, new_beams) = acc
          case set.contains(splitters, beam) {
            True -> {
              let new_beams =
                set.insert(new_beams, beam - 1)
                |> set.insert(beam + 1)
              #(count + 1, new_beams)
            }
            False -> #(count, set.insert(new_beams, beam))
          }
        })
      split_beams(new_beams, rest, new_count)
    }
  }
}

fn get_input(path) {
  let lines = utils.get_input_lines(path)
  let start_col =
    list.first(lines)
    |> result.unwrap("")
    |> utils.find_first("S", 0)

  let lines = list.drop(lines, 1)
  #(lines, start_col)
}

pub fn day7p1(path) -> Int {
  let #(lines, start_col) = get_input(path)
  let beams = set.new() |> set.insert(start_col)

  let #(res, _beams) = split_beams(beams, lines, 0)
  io.println("Day 7 part 1 : " <> int.to_string(res))
  res
}

fn count_timelines(
  pos: #(Int, Int),
  splitters: set.Set(#(Int, Int)),
  max_depth: Int,
  memo: dict.Dict(#(Int, Int), Int),
) {
  // Look at the position below
  let next_pos = #(pos.0 + 1, pos.1)

  case next_pos.0 > max_depth {
    True -> #(1, memo)
    False -> {
      case dict.has_key(memo, next_pos) {
        True -> {
          // We already counted from this pos. Just return the count
          #(dict.get(memo, next_pos) |> result.unwrap(0), memo)
        }
        False -> {
          case set.contains(splitters, next_pos) {
            True -> {
              let #(count_left, memo) =
                count_timelines(
                  #(pos.0 + 1, pos.1 - 1),
                  splitters,
                  max_depth,
                  memo,
                )
              let #(count_right, memo) =
                count_timelines(
                  #(pos.0 + 1, pos.1 + 1),
                  splitters,
                  max_depth,
                  memo,
                )
              let count = count_left + count_right
              let memo = dict.insert(memo, pos, count)
              #(count, memo)
            }
            False -> {
              count_timelines(#(pos.0 + 1, pos.1), splitters, max_depth, memo)
            }
          }
        }
      }
    }
  }
}

fn find_splitter_positions(lines, positions, row_idx) {
  case lines {
    [] -> positions
    [line, ..rest] -> {
      let splitters = find_splitters(line)
      let new_poss =
        set.fold(splitters, positions, fn(np, split_col) {
          set.insert(np, #(row_idx, split_col))
        })
      find_splitter_positions(rest, new_poss, row_idx + 1)
    }
  }
}

pub fn day7p2(path) -> Int {
  let #(lines, start_col) = get_input(path)
  let start_pos = #(0, start_col)
  let splitters = find_splitter_positions(lines, set.new(), 1)
  let max_depth = list.length(lines)
  let #(res, _memo) =
    count_timelines(start_pos, splitters, max_depth, dict.new())
  io.println("Day 7 part 2 : " <> int.to_string(res))
  res
}
