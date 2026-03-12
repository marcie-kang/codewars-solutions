"""
Description:
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples
* With input "10.0.0.0", "10.0.0.50"  => return   50
* With input "10.0.0.0", "10.0.1.0"   => return  256
* With input "20.0.0.10", "20.0.1.0"  => return  246
"""
def ips_between(start, end):
    start_IP = start.split(".")
    end_IP = end.split(".")

    start_sum = 0
    end_sum = 0

    for i in range(4):
        exponent = 3 - i

        start_sum += int(start_IP[i]) * (256 ** exponent)
        end_sum += int(end_IP[i]) * (256 ** exponent)

    return end_sum - start_sum
