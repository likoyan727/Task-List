#Coding Standards

1. Naming

  -lowercase with underscores for variables and functions (ex insert_function_name)
  -captial case for classes (ex ClassName)
  -names should be clear and descriptive in as few words as possible, and not rely on abreviations 
      (ex do not use names like wrd_ct, number_of_words_counted_in_list, etc. Instead, use names like list_word_count)
  -methods with boolean return value start with words such as "is""has""can" (ex is_not_closed)
  
2. Style
   -4 spaces per indentation
  -Additional 4 spaces to differentiate between normal indentation and hanging indentation
     (ex
     def function_name(var_one, var_two, var_four
           var_five, var_size):
         print(var_five)
         print(var_one)
      )
  -one empty line separating functions or other related blocks of code
  -leave comments above functions and classes describing their purpose and functionality

4. Pull Requests
  -All changes must be committed to a separate branch before merging with main
  -Must submit pull request with descriptive and concise explanation of the changes being suggested and why
  -Code will be reviewed based on adherence to naming and style, code functionality, and proper unit testing

5. Testing
  -Use unittest framework for unit testing
  -"import unittest" to use the framework
  -Isolate blocks of code in a separate class, with passed arugment "unittest.TestCase"
  -Define methods that start with "test"  
  -Use methods such as AssertEquals and AssertTrue to test isolated blocks of code
  *For full unittest documentation, visit https://docs.python.org/3/library/unittest.html
