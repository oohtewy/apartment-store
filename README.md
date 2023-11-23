# apartment-store
Apartment store

# I don't know
```
Python filters:
1. *safe*     => {{ variable_name|safe }}  => is used to mark a string as safe, so that it is not escaped (safe means characters like <, >, and & are not escaped but rendered as is)
2. *escape*   => {{ variable_name|escape }}  => is used to escape a string (escape means characters like <, >, and & are escaped) 
3. *lower*    => {{ variable_name|lower }}  => is used to convert a string to lowercase
4. *upper*    => {{ variable_name|upper }}  => is used to convert a string to uppercase
5. *title*    => {{ variable_name|title }}  => is used to convert a string to titlecase
6. *length*   => {{ variable_name|length }}  => is used to get the length of a string
7. *striptags* => {{ variable_name|striptags }}  => is used to remove HTML tags from a string
8. *join*     => {{ variable_name|join:" " }}  => is used to join a list of strings with a separator
9. *default*  => {{ variable_name|default:"default value" }}  => is used to set a default value if the variable is not defined
10. *date*    => {{ variable_name|date:"Y-m-d" }}  => is used to format a date
11. *time*    => {{ variable_name|time:"H:i:s" }}  => is used to format a time
12. *random*  => {{ variable_name|random }}  => is used to get a random item from a list
13. *first*   => {{ variable_name|first }}  => is used to get the first item of a list
14. *last*    => {{ variable_name|last }}  => is used to get the last item of a list
15. *length_is* => {{ variable_name|length_is:"5" }}  => is used to check if the length of a string is equal to a value
16. *slice*   => {{ variable_name|slice:"1:3" }}  => is used to get a slice of a list
... and many more
https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters


```

