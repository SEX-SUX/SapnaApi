from setuptools import setup,find_packages
import re
def version():
    filename = "SapnaApi/__init__.py"
    with open(filename) as f:
        match = re.search(r"""^__version__ = ['"]([^'"]*)['"]""", f.read(), re.M)
    if not match:
        raise RuntimeError("{} doesn't contain __version__".format(filename))
    version = match.groups()[0]
    return version
with open("README.md", encoding="utf8") as readme:
    long_desc = readme.read()
    


# Setting up
setup(
    name="SapnaApi",
    version=version(),
    author="˹ sᴀᴘɴᴀ ᴘᴏᴡᴇʀғᴜʟ ᴀᴘɪ ˼",
    author_email="sanatanixtech@gmail.com",
    description="python api hub | SapnaApi",
    long_description_content_type="text/markdown",
    long_description=long_desc,
    packages=find_packages(),
    license="MIT",
    url="https://github.com/SEX-SUX/SapnaApi",
    download_url="https://github.com/SEX-SUX/SapnaApi/blob/main/README.md",
    install_requires=["pytz>=2023.3","requests-html","pillow","lxml_html_clean"],
    keywords=['python', "SapnaApi","flask"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    
    project_urls={
        "Tracker": "https://github.com/SEX-SUX/SapnaApi/issues",
        "Community": "https://t.me/V_VIP_OWNER",
        "Source": "https://github.com/SEX-SUX/SapnaApi",
    },
    python_requires="~=3.7",
)