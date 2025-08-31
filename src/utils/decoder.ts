function decodeJWT(token: string): { header: object; payload: object } | null {
    const parts = token.split('.');
    if (parts.length !== 3) {
        return null; // Invalid JWT
    }

    const header = JSON.parse(Buffer.from(parts[0], 'base64').toString());
    const payload = JSON.parse(Buffer.from(parts[1], 'base64').toString());

    return { header, payload };
}

export { decodeJWT };