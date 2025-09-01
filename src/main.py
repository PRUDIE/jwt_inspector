#!/usr/bin/env python3
import click
import json
from .utils.decoder import decode_jwt
from .utils.validator import has_none_algorithm, validate_jwt_structure
from .utils.verifier import verify_jwt_signature

@click.command()
@click.argument('token')
@click.option('--key', help='Secret or public key for signature verification')
@click.option('--algorithm', default='HS256', help='Algorithm for signature verification')
def cli(token, key, algorithm):
    #JWT Inspector CLI - Decode, validate, and analyze JSON Web Tokens.
    
    # Validate JWT structure
    if not validate_jwt_structure(token):
        click.echo("Error: Invalid JWT structure")
        return
    
    # Decode JWT
    decoded = decode_jwt(token)
    if not decoded:
        click.echo("Error: Failed to decode JWT")
        return
    
    # Display decoded information
    click.echo("=== JWT HEADER ===")
    click.echo(json.dumps(decoded["header"], indent=2))
    
    click.echo("\n=== JWT PAYLOAD ===")
    click.echo(json.dumps(decoded["payload"], indent=2))
    
    # Check for none algorithm
    if has_none_algorithm(decoded):
        click.echo("\n WARNING: JWT uses 'none' algorithm - potential security risk!")
    
    # Verify signature if key provided
    if key:
        verified = verify_jwt_signature(token, key, algorithm)
        if verified:
            click.echo(f"\n Signature verified successfully using {algorithm}")
        else:
            click.echo(f"\n Signature verification failed using {algorithm}")

if __name__ == "__main__":
    cli()