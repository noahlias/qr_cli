
# QR Code Cli Tool

This is a simple QR Code encode and scanner project for myself to prcatice `python` and the package manageer `poetry`.
> main code is generated by `ChatGPT` and the project template builds from [**Python Discord**](https://github.com/python-discord/code-jam-template)

## Setup

```bash
poetry install
```

## Getting Started

### Encoder

```shell
qr_cli generate "hellworld" output.png
```

### Scanner

```shell
qr_cli scan output.png
```

## Problems

### _ImportError: Unable to find zbar shared library_

If you are using mac m1, you may find this problem.
Below is the [solution](https://github.com/npinchot/zbar/issues/3#issuecomment-1038005495)

```shell
mkdir ~/lib
ln -s $(brew --prefix zbar)/lib/libzbar.dylib ~/lib/libzbar.dylib
```

## Reference

- [qrcode](https://github.com/lincolnloop/python-qrcode/)
- [opencv](https://github.com/opencv/opencv-python)

## Licence

[MIT](LICENSE)
