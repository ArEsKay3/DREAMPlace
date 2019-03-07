##
# @file   setup.py
# @author Yibo Lin
# @date   Jun 2018
#

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension, CUDAExtension

import os 
import sys

ops_dir = os.environ['OPS_DIR']

cuda_flags = os.environ['CUDAFLAGS']
print("cuda_flags = %s" % (cuda_flags))

include_dirs = [os.path.abspath(ops_dir)]

setup(
        name='density_overflow',
        ext_modules=[
            CppExtension('density_overflow_cpp', 
                [
                    'density_overflow.cpp'
                    ]
                ),
            CUDAExtension('density_overflow_cuda_thread_map', 
                [
                    'density_overflow_cuda_thread_map.cpp',
                    'density_overflow_cuda_kernel.cu', 
                    'density_overflow_cuda_thread_map_kernel.cu'
                    ], 
                include_dirs=include_dirs, 
                libraries=['cusparse', 'culibos'],
                extra_compile_args={
                    'cxx': ['-O2'], 
                    'nvcc': [cuda_flags]
                    }
                ),
            CUDAExtension('density_overflow_cuda_by_node', 
                [
                    'density_overflow_cuda_by_node.cpp',
                    'density_overflow_cuda_by_node_kernel.cu'
                    ], 
                include_dirs=include_dirs, 
                libraries=['cusparse', 'culibos'],
                extra_compile_args={
                    'cxx': ['-O2'], 
                    'nvcc': [cuda_flags]
                    }
                ),
            ],
        cmdclass={
            'build_ext': BuildExtension
            })
