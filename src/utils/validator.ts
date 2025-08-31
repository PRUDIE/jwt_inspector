export function validateAlgorithm(jwt: string): boolean {
    const parts = jwt.split('.');
    if (parts.length !== 3) {
        throw new Error('Invalid JWT format');
    }

    const header = JSON.parse(Buffer.from(parts[0], 'base64url').toString());
    return header.alg !== 'none';
}