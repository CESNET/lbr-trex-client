import setuptools

setuptools.setup(
    name="lbr_trex_client",
    version="1.0",
    author="CESNET",
    author_email="tran@cesnet.cz",
    description="Lbr_trex_client contains official Cisco TRex client API as python package.",
    long_description=description,
    long_description_content_type="text/plain",
    url="https://gitlab.liberouter.org/testing/trex-client",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.6",
    ],
    python_requires='>=3.6',
)
