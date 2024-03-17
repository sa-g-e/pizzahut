# pizzahut
The algorithm that pizza hut (only in nz) uses to generate the free cheese pizza codes.


1. Start by generating a random number within the range of 1000 to 9999.
2. Then check if the generated number is divisible by 3.
3. If the number is divisible by 3, return the number with a prefix of 2, and plus 1 on the end (no idea why pizza hut does this...).
4. If it's not divisible by 3 go back to step 1.

Example:

1158 / 3 = 386 (divisible by 3),

1158 + 1 = 1159,

prefix it with 2 at the start:

21159, working code!

![image](https://github.com/sa-g-e/pizzahut/assets/58725288/bb54b70b-b2bd-4f10-bf7f-885e833b1463)
