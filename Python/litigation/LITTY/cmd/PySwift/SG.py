import PySimpleGUI as sg




def createTable(information_array:list, headings:list, key:str, tooltip:str="A simple table", maxcol:int=35,maxrows:int=10, enable_click_events:bool=True):
    table_layout = [
        [sg.Table(
            values=information_array,
            headings=headings,
            max_col_width=maxcol,
            auto_size_columns=True,
            display_row_numbers=True,
            justification="center",
            num_rows=maxrows,
            enable_click_events=enable_click_events,
            key=key,
            row_height=maxcol,
            tooltip=tooltip
        )]
    ]