// https://leetcode.com/problems/remove-vowels-from-a-string



char * removeVowels(char * s){
    char p[strlen(s)];

    int j = 0;
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
            continue;
        }
        p[j] = s[i];
        j++;
    }

    p[j] = '\0';
    strncpy(s, p, strlen(s));
    return s;
}