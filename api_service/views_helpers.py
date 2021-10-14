

def set_summary(ws, columns_found, summary):
    calculate = False
    for col_idx in range(ws.max_column):
        for row in range(1, ws.max_row+1):
            if type(ws[row][col_idx].value) == str and ws[row][col_idx].value.strip() in columns_found.keys()\
                    and calculate is False:
                col_name = ws[row][col_idx].value.strip()
                columns_found[col_name] = True
                summary_element = {"column": col_name}
                sum = 0
                counter = 0
                calculate = True
            if calculate is True:
                if type(ws[row][col_idx].value) in [float, int]:
                    sum += ws[row][col_idx].value
                    counter += 1
                if (row == ws.max_row or type(ws[row+1][col_idx].value) is str) and counter > 0:
                    summary_element["sum"] = round(sum, 2)
                    summary_element["avg"] = round(sum/counter, 2)
                    calculate = False
                    summary.append(summary_element)
        calculate = False
