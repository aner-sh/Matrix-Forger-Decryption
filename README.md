# matrix-forger-decryption

The forger who is forging magnetic cards has begun operating in the city. During a police raid on one of his locations, a faulty machine was found, which had previously been used to create the forgeries. Police investigators believe the forger deliberately sabotaged the machine so that the forged magnetic cards in his possession could not be traced back to the original machine.

The detectives discovered the following:

A magnetic cipher is made up of an N × N matrix, where N is a power of 2. Each cell in the matrix contains either 1 or 0.

Through investigating the faulty machine, the detectives were able to reconstruct the algorithm that the machine used:

If the cipher is a single pixel, the machine forges it according to the original cipher.
Otherwise, the matrix is divided into four smaller squares, and:
One square is filled entirely with the number 0.
One of the other three squares is filled entirely with the number 1.
The machine treats the other two remaining squares as new ciphers and repeats the algorithm for each one.
The investigators concluded that the machine cannot create a perfect forgery for every cipher. Therefore, the forger also holds incomplete ciphers.

We define the forgery discrepancy as the number of differing bits between the original cipher and the forged cipher.

It is possible that the forgery is not unique, and any forgery with a minimal discrepancy will be accepted, so the police can catch the forger when trying to use these forgeries.

In the machine found by the police, there is a history of original ciphers that have been forged.

For each original cipher found in the machine's history, find the forged cipher that has the minimal forgery discrepancy. Assume that all cards in the forger's possession have the minimal forgery discrepancy.
