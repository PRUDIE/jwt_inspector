# JWT Inspector CLI

JWT Inspector CLI is a command-line tool designed to decode, validate, and analyze JSON Web Tokens (JWTs). This tool is particularly useful for security professionals and developers who need to inspect JWTs during web application penetration tests.

## Features

- Decode Payload and Header: Easily decode the header and payload of a JWT to inspect its contents.
- Check for None Algorithm: Validate if the JWT uses the "none" algorithm, which can indicate potential security issues.
- Signature Verification*: Verify the signature of the JWT if the secret or public key is known, ensuring the token's integrity.

## Installation

To install the JWT Inspector CLI, clone the repository and install the dependencies:

```bash
git clone https://github.com/PRUDIE/jwt-inspector.git
cd jwt-inspector-cli
pip install -r requirements.txt
```

## Usage

After installation, you can run the CLI tool using the following command:

```bash
python -m src.main <jwt-token> --key <your-secret-or-public-key>
```

Replace `<jwt-token>` with the JWT you want to inspect and `<your-secret-or-public-key>` with the key used for signature verification.

## Example

To decode a JWT:

```bash
python -m src.main eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

To verify a JWT signature:

```bash
python -m src.main <jwt-token> --key <your-secret-or-public-key>
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

all other inquiries - cyberprudie@gmail.com

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
