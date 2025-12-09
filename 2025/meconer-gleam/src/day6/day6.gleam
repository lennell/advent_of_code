import gleam/int
import gleam/io
import gleam/list
import gleam/result
import gleam/string
import utils

pub fn get_input(path) {
  utils.get_input_lines(path)
  |> list.map(string.trim)
  |> list.map(fn(s) { string.replace(s, "  ", " ") })
  |> list.map(fn(s) { string.replace(s, "  ", " ") })
  |> list.map(fn(s) { string.replace(s, "  ", " ") })
  |> list.map(fn(s) { string.replace(s, "  ", " ") })
  |> list.map(fn(s) { string.replace(s, "  ", " ") })
  |> list.map(fn(s) { string.split(s, " ") })
}

pub fn calc_cols(
  lines: List(List(Int)),
  operators: List(String),
  acc: List(Int),
) -> List(Int) {
  case list.is_empty(list.first(lines) |> result.unwrap([])) {
    True -> acc
    False -> {
      let cols =
        list.fold(lines, [], fn(firsts, lst) {
          [list.first(lst) |> result.unwrap(-1), ..firsts]
        })
      let new_lines = list.map(lines, fn(line) { list.drop(line, 1) })
      let operator = list.first(operators) |> result.unwrap("")
      let new_operators = list.drop(operators, 1)
      let value = case operator {
        "+" -> list.fold(cols, 0, fn(a, n) { a + n })
        "*" -> list.fold(cols, 1, fn(a, n) { a * n })
        _ -> panic as "Err operator"
      }
      calc_cols(new_lines, new_operators, [value, ..acc])
    }
  }
}

pub fn day6p1(path) -> Int {
  let lines = get_input(path)
  let operators = list.last(lines) |> result.unwrap([])
  let lines =
    list.take(lines, list.length(lines) - 1)
    |> list.map(fn(l) {
      list.map(l, fn(s) { int.parse(s) |> result.unwrap(-1) })
    })
  let cols = calc_cols(lines, operators, [])
  let res = list.fold(cols, 0, fn(acc, n) { acc + n })

  io.println("Day 6 part 1 : " <> int.to_string(res))
  res
}

fn find_first(s: String, ch: String, idx: Int) {
  case string.is_empty(s) {
    True -> -1
    False -> {
      case string.starts_with(s, ch) {
        True -> idx
        False -> find_first(string.drop_start(s, 1), ch, idx + 1)
      }
    }
  }
}

pub fn find_idx_of_second_op(operators: String) -> Int {
  let op2 = string.drop_start(operators, 1)

  let idx_plus = find_first(op2, "+", 0)
  let idx_times = find_first(op2, "*", 0)
  case idx_plus == -1 {
    True ->
      case idx_times == -1 {
        True -> -1
        False -> idx_times
      }
    False ->
      case idx_times == -1 {
        True -> idx_plus
        False -> int.min(idx_plus, idx_times)
      }
  }
}

pub fn get_ceph_numbers(cols: List(String), acc: List(Int)) -> List(Int) {
  let col_len = list.first(cols) |> result.unwrap("") |> string.length
  case col_len {
    0 -> acc
    _ -> {
      let first = case list.first(cols) {
        Ok(f) -> f
        Error(_) -> panic as ""
      }
      let new_cols = list.map(cols, fn(col) { string.drop_end(col, 1) })
      let len = string.length(first)
      let last_cols = list.map(cols, fn(col) { string.slice(col, len - 1, 1) })
      let number_str = string.join(last_cols, "") |> string.trim
      let number = int.parse(number_str) |> result.unwrap(-1)
      get_ceph_numbers(new_cols, [number, ..acc])
    }
  }
}

pub fn calc_cols2(
  lines: List(String),
  operators: String,
  acc: List(Int),
) -> List(Int) {
  case string.is_empty(operators) {
    True -> acc
    False -> {
      let operator = string.first(operators) |> result.unwrap("")
      let idx = find_idx_of_second_op(operators)

      case idx < 0 {
        True -> {
          // Last operator
          let numbers = get_ceph_numbers(lines, [])
          let col_res = case operator {
            "*" -> list.fold(numbers, 1, fn(acc, n) { acc * n })
            "+" -> list.fold(numbers, 0, fn(acc, n) { acc + n })
            _ -> panic as "Wrong operator"
          }
          [col_res, ..acc]
        }
        False -> {
          let new_operators = case idx < 0 {
            False -> {
              string.drop_start(operators, idx + 1)
            }
            True -> ""
          }
          let new_lines = case idx < 0 {
            False ->
              list.map(lines, fn(line) { string.drop_start(line, idx + 1) })
            True -> lines
          }
          let cols = list.map(lines, fn(line) { string.slice(line, 0, idx) })
          let numbers = get_ceph_numbers(cols, [])
          let col_res = case operator {
            "*" -> list.fold(numbers, 1, fn(acc, n) { acc * n })
            "+" -> list.fold(numbers, 0, fn(acc, n) { acc + n })
            _ -> panic as "Wrong operator"
          }
          calc_cols2(new_lines, new_operators, [col_res, ..acc])
        }
      }
    }
  }
}

pub fn day6p2(path) -> Int {
  let lines = utils.get_input_lines(path)
  let operators = list.last(lines) |> result.unwrap("")
  let lines = list.take(lines, list.length(lines) - 1)
  let res =
    calc_cols2(lines, operators, []) |> list.fold(0, fn(acc, n) { acc + n })
  io.println("Day 6 part 2 : " <> int.to_string(res))
  res
}
