from setuptools import setup

dependencies = [
    "multidict==5.1.0",  # Avoid 5.2.0 due to Avast
    "blspy==1.0.6",  # Signature library
    "chiavdf==1.0.3",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.6",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.15",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the two processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspythonchia==2.2.0",  # Query DNS seeds
    "watchdog==2.1.6",  # Filesystem event watching - watches keyring.yaml
    "nest-asyncio==1.5.1",
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "types-setuptools",
]

kwargs = dict(
    name="two-blockchain",
    author="two",
    author_email="admin@twochain.top",
    description="Two blockchain full node, farmer, timelord, and wallet.",
    url="https://twochain.top/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="two blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "two",
        "two.cmds",
        "two.clvm",
        "two.consensus",
        "two.daemon",
        "two.full_node",
        "two.timelord",
        "two.farmer",
        "two.harvester",
        "two.introducer",
        "two.plotters",
        "two.plotting",
        "two.pools",
        "two.protocols",
        "two.rpc",
        "two.server",
        "two.simulator",
        "two.types.blockchain_format",
        "two.types",
        "two.util",
        "two.wallet",
        "two.wallet.puzzles",
        "two.wallet.rl_wallet",
        "two.wallet.cc_wallet",
        "two.wallet.did_wallet",
        "two.wallet.settings",
        "two.wallet.trading",
        "two.wallet.util",
        "two.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "two = two.cmds.two:main",
            "two_wallet = two.server.start_wallet:main",
            "two_full_node = two.server.start_full_node:main",
            "two_harvester = two.server.start_harvester:main",
            "two_farmer = two.server.start_farmer:main",
            "two_introducer = two.server.start_introducer:main",
            "two_timelord = two.server.start_timelord:main",
            "two_timelord_launcher = two.timelord.timelord_launcher:main",
            "two_full_node_simulator = two.simulator.start_simulator:main",
        ]
    },
    package_data={
        "two": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "two.util": ["initial-*.yaml", "english.txt"],
        "two.ssl": ["two_ca.crt", "two_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)  # type: ignore
