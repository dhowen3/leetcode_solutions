class Solution:
    def get_row_assignment(self, current_index: int, num_rows: int) -> int:
        # 2 quick base cases then general solution after
        if num_rows == 1:
            return 0
        if num_rows == 2:
            return current_index % 2
        # general solution for num_rows > 2
        cycle_length : int = 2 * num_rows - 2
        place_in_cycle : int = current_index % cycle_length
        if place_in_cycle < num_rows:
            return place_in_cycle
        else:
            place_in_zag : int = place_in_cycle - num_rows
            return num_rows - 2 - place_in_zag

    def make_2d_array(self, input_str : str, num_rows : int) -> List[List[chr]]:
        # initialize 2d array
        to_return = []
        for i in range(num_rows):
            to_return.append([])
        # assign s to rows
        for i in range(len(input_str)):
            row_assignment: int = self.get_row_assignment(i, num_rows) 
            current_char: chr = input_str[i]
            to_return[row_assignment].append(current_char)
        return to_return


    def flatten_2d_array(self, arr: List[List[chr]]) -> str:
        to_return: str = ""
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                to_return += arr[i][j]
        return to_return

    def convert(self, s: str, num_rows: int) -> str:
        arr_2d : List[List[chr]] = self.make_2d_array(s, num_rows)
        return self.flatten_2d_array(arr_2d)
