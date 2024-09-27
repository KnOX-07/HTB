#include <stdio.h>
#include <stdlib.h>

int read_file(char *name, char **buff)
{
    FILE *file;
    int sz;

    file = fopen(name, "rb");
    fseek(file, 0, SEEK_END);
    sz = ftell(file);
    rewind(file);
    *buff = (char *)calloc(sz + 1, 1);
    fread(*buff, 1, sz, file);
    fclose(file);

    return sz;
}

int main()
{
    char *buff;
    int i, r1, r2, size;

    size = read_file("flag.enc", &buff);

    r1 = *(int *)buff;
    srand(r1);
    printf("%d\n", r1);
    for (i = 4; i < size; ++i)
    {
        r1 = rand();
        r2 = rand() & 7;
        buff[i] = (buff[i] << (8 - r2)) | ((unsigned char)buff[i] >> r2);
        buff[i] ^= r1;
    }
    printf("%s\n", &buff[4]);

    free(buff);
}
