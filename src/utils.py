
import geopandas as gp
import pandas as pd

# 'line_is_in_range()' controlla che per ogni punto della linea questi non escano dal range

def point_is_in_range(point, bounds) -> bool:
    point_x, point_y = point
    return not (point_y > bounds[0] or point_y < bounds[1] or point_x < bounds[2] or point_x > bounds[3])

def line_is_in_range(lines, bounds) -> bool:
    for point in parse_geojson_linestring(lines): 
        if not point_is_in_range(point, bounds): 
            return False

    return True

def remove_lines_out_of_range(geodf : gp.GeoDataFrame, bounds) -> pd.Series: 
    res_ls = []
    for line in geodf: 
        res_ls.append(line_is_in_range(line, bounds))

    return pd.Series(res_ls)


def parse_geojson_linestring(linestr) -> list: # -> return LIST<(double, double)>
    # prendo tutti i valori tranne il primo, che è la stringa LINESTRING
    value_list = str(linestr)[12:][:-1].split(", ")
    
    tuple_list = []
    for val in value_list: 
        x, y = val.split(" ")
        tuple_list.append((float(x), float(y)))
    
    return tuple_list

def parse_geojson_point(point) -> tuple: # -> return (double, double)
    value_list = str(point)[7:][:-1].split(" ")
    return (float(value_list[0]), float(value_list[1]))