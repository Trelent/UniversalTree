from utree import nodes

def encode_ts_nodes(document: str, node_type: str, ts_nodes):
    children_count = 0
    if node_type == "class":
        children_count = 3
    elif node_type == "function":
        children_count = 4
    elif node_type == "method":
        children_count = 4
    else:
        return []

    if len(ts_nodes) == 0:
        return []

    # Let's first sort the ts_nodes by start_point and end_point
    ts_nodes.sort(key=lambda x: (x[0].start_point[0], x[0].start_point[1], x[0].end_point[0], x[0].end_point[1]))

    # Check if we have multiple matches, and divide them into separate node groups
    # as necessary. Eg. 3 ts_nodes represent a single class object, so if we have
    # multiple classes, we need to split a group of (n*3) nodes into n groups.
    n = len(ts_nodes) // children_count
    node_groups = []
    for x in range(n):
        current_group = []
        for y in range(children_count):
            current_group.append(ts_nodes[x*children_count + y])
        node_groups.append(current_group)
    
    # Debug
    # print(str(n) + " group(s) of " + str(children_count) + " node(s)")
    # print(node_groups)
    
    resultant_objects = []
    for node_group in node_groups:
        node_object = _encode_single_ts_node(document, node_type, node_group)
        if(node_object is not None):
            resultant_objects.append(node_object)

    return resultant_objects

def _encode_single_ts_node(document: str, node_type: str, ts_nodes):
    """
    Enode a single tree-sitter node into a UTree object of type `node_type`.
    """
    if(node_type == "class"):
        return _encode_class_ts_node(document, ts_nodes)
    elif(node_type == "function"):
        return _encode_function_ts_node(document, ts_nodes)
    elif(node_type == "method"):
        return _encode_method_ts_node(document, ts_nodes)
    else:
        return None
    

def _encode_class_ts_node(document: str, ts_nodes):
    """
    Encode a single tree-sitter node into a UTree Class object.
    """
    node_name = ""
    node_start = nodes.Point(-1, -1)
    node_end = nodes.Point(-1, -1)
    node_text = ""

    for ts_node in ts_nodes:
        node_type = ts_node[1]
        start_point = nodes.Point(ts_node[0].start_point[0], ts_node[0].start_point[1])
        end_point = nodes.Point(ts_node[0].end_point[0], ts_node[0].end_point[1])

        if node_type == "class.def":
            node_text = _extract_text_from_range(document, start_point, end_point)
            node_start = start_point
            node_end = end_point
        elif node_type == "class.name":
            node_name = _extract_text_from_range(document, start_point, end_point)

    return nodes.Class(node_name, node_start, node_end, node_text)

def _encode_function_ts_node(document: str, ts_nodes):
    """
    Encode a single tree-sitter Function node into a UTree Function object.
    """
    if len(ts_nodes) == 0:
        return None

    func_name = ""
    func_start = nodes.Point(-1, -1)
    func_end = nodes.Point(-1, -1)
    func_text = ""
    func_params = []
    func_definition = ""
    func_body = ""


    for ts_node in ts_nodes:
        node_type  = ts_node[1]
        node_start = nodes.Point(ts_node[0].start_point[0], ts_node[0].start_point[1])
        node_end   = nodes.Point(ts_node[0].end_point[0], ts_node[0].end_point[1])

        if node_type == "function.def":
            func_start = node_start
            func_end = node_end
        elif node_type == "function.name":
            func_name = _extract_text_from_range(document, node_start, node_end)
        elif node_type == "function.params":
            param_text = _extract_text_from_range(document, node_start, node_end)
            func_params = _extract_params_from_text(param_text)
        elif node_type == "function.body":
            func_definition = _extract_text_from_range(document, func_start, node_start).rstrip()
            func_body = _extract_text_from_range(document, node_start, node_end)

    return nodes.Function(func_body, func_definition, nodes.Docstring(False, None, None, None), func_name, func_params)

def _encode_method_ts_node(document: str, ts_nodes):
    """
    Encode a single tree-sitter Method node into a UTree Method object.
    """
    if len(ts_nodes) == 0:
        return None

    func_name = ""
    func_start = nodes.Point(-1, -1)
    func_end = nodes.Point(-1, -1)
    func_text = ""
    func_params = []
    func_definition = ""
    func_body = ""
    parent_start = nodes.Point(-1, -1)
    parent_end = nodes.Point(-1, -1)
    parent_name = ""
    parent_text = ""


    for ts_node in ts_nodes:
        node_type  = ts_node[1]
        node_start = nodes.Point(ts_node[0].start_point[0], ts_node[0].start_point[1])
        node_end   = nodes.Point(ts_node[0].end_point[0], ts_node[0].end_point[1])

        if node_type == "method.def":
            func_start = node_start
            func_end = node_end
        elif node_type == "method.name":
            func_name = _extract_text_from_range(document, node_start, node_end)
        elif node_type == "method.params":
            param_text = _extract_text_from_range(document, node_start, node_end)
            func_params = _extract_params_from_text(param_text)
        elif node_type == "method.body":
            func_definition = _extract_text_from_range(document, func_start, node_start).rstrip()
            func_body = _extract_text_from_range(document, node_start, node_end)
        #elif node_type == "class.def":
        #    parent_text = _extract_text_from_range(document, node_start, node_end)
        #    parent_start = node_start
        #    parent_end = node_end
        #elif node_type == "class.name":
        #    parent_name = _extract_text_from_range(document, node_start, node_end)

    #parent = nodes.Class(parent_name, parent_start, parent_end, parent_text)

    return nodes.Method(func_body, func_definition, nodes.Docstring(False, None, None, None), func_name, func_params)

def _extract_params_from_text(param_text: str):
    params = []
    param_list = param_text.split(",")
    for param in param_list:
        param = param.strip()
        if param == "":
            continue
        params.append(param)
    return params

def _extract_text_from_range(document: str, start: nodes.Point, end: nodes.Point) -> str:
    start_line = start.line
    start_col  = start.col

    end_line = end.line
    end_col = end.col

    lines = document.split("\n")
    line_count = len(lines)
    if start_line >= line_count:
        return ""

    if start_line == end_line:
        return lines[start_line][start_col:end_col]

    return lines[start_line][start_col:] + "\n" + "\n".join(lines[start_line + 1:end_line]) + "\n" + lines[end_line][:end_col]