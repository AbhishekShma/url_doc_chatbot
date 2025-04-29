def split_output_string(string):
    result_of_split = string.rsplit("<|end_header_id|>", -1)
    return result_of_split[-1]

def format_llm_output(result: str):
    result = split_output_string(result)
    return result
