import gleam/int
import gleam/string
import simplifile

pub fn read_input(file_path: String) -> String {
  case simplifile.read(file_path) {
    Ok(content) -> string.trim(content)
    Error(_) -> "Error reading file"
  }
}

pub fn get_input_lines(path: String) -> List(String) {
  read_input(path)
  |> string.trim
  |> string.split("\n")
}

pub fn safe_int_parse(s: String) -> Int {
  case int.parse(s) {
    Ok(i) -> i
    Error(_) -> panic as "Invalid int"
  }
}

pub fn find_first(s: String, ch: String, idx: Int) {
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
