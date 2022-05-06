%{
    #include<math.h>  
%}
DIG [0-9]
ID [a-zA-Z]
%%

#.* {printf("\n%s Header File",yytext);}
{DIG}+ {
    printf("%s is a number\n",yytext);
}
int|float|if|else|for|while|do|switch|void|main|char|printf|scanf {
    printf("%s is a Key Word\n",yytext);
}
{ID} {
    printf("%s is a Identifier\n",yytext);
}
"+"|"-"|"*"|"/"|"="|"<"|">" {
    printf("%s is a Operator\n",yytext);
}
";"|"{"|"}"|","|"("|")"|"["|"]" {
    printf("%s is a Special Symbol\n",yytext);
}


%%
int yywrap(){}
void main()
{
    FILE *fp;
    fp = fopen("var.c","r");
    yyin = fp;
    yylex();
}