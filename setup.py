import setuptools

setuptools.setup(
    name="lbr_trex_client",
    version="2.0.1",
    author="CESNET",
    author_email="tran@cesnet.cz",
    description="Lbr_trex_client contains official Cisco TRex client API as python package.",
    url="https://gitlab.liberouter.org/testing/trex-client",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.6",
    ],
    python_requires='>=3.6',
)
