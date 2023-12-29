#------------------------------------------------------------------------------
# Hands-On Lab: Data Engineering with Snowpark
# Script:       05_multiplication_udf/app.py
# Author:       Kaulab Basu
# Last Updated: 12/23/2023
#------------------------------------------------------------------------------

# SNOWFLAKE ADVANTAGE: Snowpark Python programmability
# SNOWFLAKE ADVANTAGE: Python UDFs (with third-party packages)
# SNOWFLAKE ADVANTAGE: SnowCLI (PuPr)

import sys

def main(digit: float) -> float:
    return (float(digit)*float(digit))

# For local debugging
# Be aware you may need to type-convert arguments if you add input parameters
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(*sys.argv[1:]))  # type: ignore
    else:
        print(main())  # type: ignore
