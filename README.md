# Bug report for Nuitka

This is reproduction code for a bug in Nuitka, where running the same code with
CPython and Nuitka produces different results.

In CPython, the exception from gRPC is caught with appropriate details, while
in Nuitka-compiled code, we get an async-related error.

## Steps to reproduce

Easiest way to reproduce it via docker compose:

```bash
docker compose up --build
```
