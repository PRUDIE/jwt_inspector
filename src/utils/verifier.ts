export function verifySignature(jwt: string, key: string): boolean {
    const [header, payload, signature] = jwt.split('.');
    if (!header || !payload || !signature) {
        return false;
    }

    const data = `${header}.${payload}`;
    const decodedSignature = Buffer.from(signature, 'base64').toString('utf8');

    // Implement signature verification logic here
    // This is a placeholder for actual verification logic
    const isValid = decodedSignature === 'expectedSignature'; // Replace with actual verification

    return isValid;
}