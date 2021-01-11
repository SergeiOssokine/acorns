from __future__ import absolute_import
__version__ = '0.0.4'
__all__ = [
    'autodiff', 'unroll_file', 'unroll', 
]

from .forward_diff import prepare_graph as prep_graph_ad
from .forward_diff import grad, grad_with_split
from .unroll import prepare_graph_from_file, prepare_graph


def autodiff(function, expression, variables, func = 'function', 
                reverse_diff = False, second_der = False, output_filename = 'c_code',
                output_func = 'compute', split=False, split_by=20, parallel = False, num_threads = 1,
             differentiate_pow_exp = True):


    ast = prep_graph_ad(function)

    if split:
        grad_with_split(ast, expression, variables, func = func, 
            reverse_diff = reverse_diff, second_der = second_der, output_filename = output_filename, 
            output_func = output_func, split_by=split_by, parallel = parallel, num_threads = num_threads,
            differentiate_pow_exp = differentiate_pow_exp)
    else:
        grad(ast, expression, variables, func = func, 
            reverse_diff = reverse_diff, second_der = second_der, output_filename = output_filename, 
            output_func = output_func, parallel = parallel, num_threads = num_threads,
            differentiate_pow_exp = differentiate_pow_exp)


def unroll_file(filename, output_filename,  constants = []):
	ast  = prepare_graph_from_file(filename, output_filename, constants_list=constants)
	return ast

def unroll(function, output_filename, constants = []):
	ast = prepare_graph(function, output_filename, constants_list=constants)
	return ast
