
import geopandas as gp
import pandas as pd

# La funzione è usata per eseguire selezioni su dataframe contenenti POINT()
# in base a bounds passati per argomento
# data[remove_points_out_of_range(data['field'], BOUNDS)]
# restituisce una serie pd.Series<Boolean> 
def remove_points_out_of_range(geodf : gp.GeoDataFrame, bounds) -> pd.Series: 
    res_ls = []
    for pointstr in geodf: 
        res_ls.append(
            point_is_in_range(
                parse_geojson_point(pointstr), 
                bounds
                ))
    return pd.Series(res_ls)

# Controlla se un punto è all'interno dei bounds
def point_is_in_range(point, bounds) -> bool:
    point_x, point_y = point
    return not (point_y > bounds[0] or point_y < bounds[1] or point_x < bounds[2] or point_x > bounds[3])

# Controlla se ogni punto della linea è nei bounds
def line_is_in_range(lines, bounds) -> bool:
    for point in parse_geojson_linestring(lines): 
        if not point_is_in_range(point, bounds): 
            return False

    return True

# La funzione è da usare per eseguire selezioni su dataframe contenenti LINESTRING()
# in base ai BOUNDS
# data[remove_lines_out_of_range(data['field'], BOUNDS)]
# restituisce una serie -> pd.Series<Boolean> 
def remove_lines_out_of_range(geodf : gp.GeoDataFrame, bounds) -> pd.Series: 
    res_ls = []
    for line in geodf: 
        res_ls.append(line_is_in_range(line, bounds))

    return pd.Series(res_ls)

# Converte una stringa in formato LINESTRING(x1 y1, x2 y2...)
# in una lista di tuple [(x1, y1), (x2, y2), ...] 
def parse_geojson_linestring(linestr) -> list: # -> return LIST<(double, double)>
    # prendo tutti i valori tranne il primo, che è la stringa LINESTRING(
    # e la parentesi finale 
    value_list = str(linestr)[12:][:-1].split(", ")
    
    tuple_list = []
    for val in value_list: 
        # aggiungo i punti come tuple (tutti quelli della linea)
        x, y = val.split(" ")
        tuple_list.append((float(x), float(y)))
    
    return tuple_list

# Converte una stringa in formato POINT(x y) in una tupla (x, y)
def parse_geojson_point(point) -> tuple: # -> return (float, float)
    # la struttura è POINT(x, y), devo eliminare la stringa POINT( e la parentesi finale
    value_list = str(point)[7:][:-1].split(" ")
    return (float(value_list[0]), float(value_list[1]))