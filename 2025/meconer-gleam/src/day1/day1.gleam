import gleam/int
import gleam/io
import gleam/list
import gleam/string
import utils

pub fn day1p1(path) -> Int {
  let #(cnt, _pos) =
    utils.get_input_lines(path)
    |> list.fold(#(0, 50), fn(acc, line) {
      let dir = case string.first(line) {
        Ok(c) -> c
        Error(_) -> ""
      }
      let delta_str = string.slice(line, 1, string.length(line))
      let delta = case int.parse(delta_str) {
        Ok(n) -> n
        Error(_) -> 0
      }
      let new_pos = case dir {
        "L" -> { acc.1 - delta } % 100
        "R" -> { acc.1 + delta } % 100
        _ -> panic as "Invalid direction"
      }
      case new_pos {
        0 -> #(acc.0 + 1, new_pos)
        _ -> #(acc.0, new_pos)
      }
    })
  io.println("Day 1, Part 1 : " <> int.to_string(cnt))
  cnt
}

pub fn day1p2(path) -> Int {
  let #(cnt, _pos) =
    utils.get_input_lines(path)
    |> list.fold(#(0, 50), fn(acc, line) {
      let dir = case string.first(line) {
        Ok(c) -> c
        Error(_) -> ""
      }
      let delta =
        string.slice(line, 1, string.length(line)) |> utils.safe_int_parse
      let #(cnt, pos) = acc
      let whole_turns = delta / 100
      let delta_rest = delta % 100
      let #(new_cnt, new_pos) = case dir {
        "L" ->
          case delta_rest > pos {
            True ->
              case pos {
                0 -> #(whole_turns + cnt, pos - delta_rest + 100)
                _ -> #(1 + whole_turns + cnt, pos - delta_rest + 100)
              }
            False -> #(whole_turns + cnt, pos - delta_rest)
          }
        "R" ->
          case delta_rest + pos > 100 {
            True -> #(1 + whole_turns + cnt, { pos + delta_rest } % 100)
            False -> #(whole_turns + cnt, { pos + delta_rest } % 100)
          }
        _ -> panic as "Invalid direction"
      }
      let res = case new_pos {
        0 -> #(new_cnt + 1, new_pos)
        _ -> #(new_cnt, new_pos)
      }
      res
    })
  io.println("Day 1, Part 2 : " <> int.to_string(cnt))
  //5936 too low
  cnt
}
