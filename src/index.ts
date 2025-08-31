import { decodeJWT } from './utils/decoder';
import { validateAlgorithm } from './utils/validator';
import { verifySignature } from './utils/verifier';

const args = process.argv.slice(2);
const jwt = args[0];
const secretOrPublicKey = args[1];

if (!jwt) {
    console.error('Please provide a JWT to inspect.');
    process.exit(1);
}

const { header, payload } = decodeJWT(jwt);
console.log('Decoded Header:', header);
console.log('Decoded Payload:', payload);

const isValidAlgorithm = validateAlgorithm(header.alg);
if (!isValidAlgorithm) {
    console.warn('Warning: The JWT uses the "none" algorithm, which is insecure.');
}

if (secretOrPublicKey) {
    const isSignatureValid = verifySignature(jwt, secretOrPublicKey);
    console.log('Signature Valid:', isSignatureValid);
} else {
    console.log('No secret or public key provided for signature verification.');
}