import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="package_poc",
    version="0.0.1",
    author="Ivan Pinojtic",
    author_email="ivan.pinojtic@glooko.com",
    description="Testing installation of Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IvanPGlooko/package_poc",
    project_urls = {
        "Bug Tracker": "https://github.com/IvanPGlooko/package_poc/issues"
    },
    license="MIT",
    packages=["poc_folder"],
    install_requires=[],
)