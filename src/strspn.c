int
strspn(const char *p, const char *s)
{
    int i, j;

    for (i = 0; p[i]; i++) {
        for (j = 0; s[j]; j++) {
            if (s[j] == p[i])
                break;
        }
        if (!s[j])
            break;
    }
    return (i);
}
