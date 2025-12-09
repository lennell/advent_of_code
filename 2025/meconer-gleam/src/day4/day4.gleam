import gleam/dict
import gleam/int
import gleam/io
import gleam/list
import gleam/result
import gleam/string
import utils

pub fn get_grid(path) {
  let input = utils.get_input_lines(path)
  let height = list.length(input)
  let first_line = list.first(input) |> result.unwrap("")
  let width = string.length(first_line)
  let #(_, grid) =
    list.fold(input, #(#(0, 0), dict.new()), fn(acc, str) {
      let cols = string.to_graphemes(str)
      let #(_, col_dict) =
        list.fold(cols, acc, fn(inn_acc, el) {
          let #(#(row, col), mtx_dict) = inn_acc
          #(#(row, col + 1), dict.insert(mtx_dict, #(row, col), el))
        })
      let #(#(row, _col), mtx_dict) = acc
      #(#(row + 1, 0), dict.merge(mtx_dict, col_dict))
    })
  #(height, width, grid)
}

pub fn get_el(grid, coord) {
  dict.get(grid, coord) |> result.unwrap(".")
}

fn get_neighbours(grid, coord) {
  let #(row, col) = coord
  let neighbour_coords = [
    #(row - 1, col - 1),
    #(row - 1, col),
    #(row - 1, col + 1),
    #(row, col - 1),
    #(row, col + 1),
    #(row + 1, col - 1),
    #(row + 1, col),
    #(row + 1, col + 1),
  ]
  list.map(neighbour_coords, fn(coord) { get_el(grid, coord) })
}

fn count_neighbour_rolls(grid, coord) {
  list.fold(get_neighbours(grid, coord), 0, fn(cnt, el) {
    case el == "@" {
      True -> cnt + 1
      False -> cnt
    }
  })
}

pub fn day4p1(path) -> Int {
  let #(height, width, grid) = get_grid(path)

  let res =
    list.fold(list.range(0, height - 1), 0, fn(cnt, row) {
      list.fold(list.range(0, width - 1), cnt, fn(cnt, col) {
        case get_el(grid, #(row, col)) == "@" {
          True -> {
            //Count only if there is a roll here
            case count_neighbour_rolls(grid, #(row, col)) < 4 {
              True -> cnt + 1
              False -> cnt
            }
          }
          False -> cnt
        }
      })
    })

  io.println("Day 4 part 1 : " <> int.to_string(res))
  res
}

fn count_rolls(grid, height, width) {
  list.fold(list.range(0, height - 1), 0, fn(cnt, row) {
    list.fold(list.range(0, width - 1), cnt, fn(cnt, col) {
      case get_el(grid, #(row, col)) == "@" {
        True -> cnt + 1
        False -> cnt
      }
    })
  })
}

fn rec_remove_rolls(grid, height, width) {
  let #(did_remove, new_grid) =
    list.fold(list.range(0, height - 1), #(False, grid), fn(acc, row) {
      list.fold(list.range(0, width - 1), acc, fn(acc, col) {
        let #(did_remove, grid) = acc
        case get_el(grid, #(row, col)) == "@" {
          True -> {
            let neighbour_cnt = count_neighbour_rolls(grid, #(row, col))
            case neighbour_cnt < 4 {
              True -> {
                // Remove this roll
                #(True, dict.delete(grid, #(row, col)))
              }
              False -> #(did_remove, grid)
            }
          }
          False -> #(did_remove, grid)
        }
      })
    })
  case did_remove {
    True -> rec_remove_rolls(new_grid, height, width)
    False -> new_grid
  }
}

pub fn day4p2(path) -> Int {
  let #(height, width, grid) = get_grid(path)

  let initial_roll_count = count_rolls(grid, height, width)
  let new_grid = rec_remove_rolls(grid, height, width)
  let remainining_roll_count = count_rolls(new_grid, height, width)
  let res = initial_roll_count - remainining_roll_count
  io.println("Day 4 part 2 : " <> int.to_string(res))
  res
}
