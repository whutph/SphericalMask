from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


if __name__ == "__main__":
    setup(
        name="spherical_mask",
        version="1.0",
        description="spherical_mask",
        author="sangyun shin",
        packages=find_packages(),
        package_data={"spherical_mask.ops": ["*/*.so"]},
        install_requires=[
            "pointnet2",  # Add pointnet2 as a dependency
        ],
        ext_modules=[
            CUDAExtension(
                name="spherical_mask.ops.ops",
                sources=[
                    "spherical_mask/ops/src/isbnet_api.cpp",
                    "spherical_mask/ops/src/isbnet_ops.cpp",
                    "spherical_mask/ops/src/cuda.cu",
                ],
                extra_compile_args={"cxx": ["-g"], "nvcc": ["-O2",
                "-gencode=arch=compute_80,code=sm_80"]},
            )
        ],
        cmdclass={"build_ext": BuildExtension},
    )
