import numpy

def elementwise_relu(matrix_):
    '''
    the relu operation: max(x, 0)
    is looping through the entire matrix
    and setting the result to replace the 
    existing value

    this is technically equivalent to
    numpy.maximum(x, 0). typically
    numpy.maximum is designed to
    compare two matrices.
    '''
    assert matrix_.ndim == 2

    matrix_ = matrix_.copy()
    row_size, col_size = numpy.shape(matrix_)
    for row in range(row_size):
        for col in range(col_size):
            matrix_[row, col] = max(matrix_[row, col], 0)
    
    return matrix_

