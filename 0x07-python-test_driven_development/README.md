## Python - Test-driven development

### Learning Objectives
A. What’s an interactive test

	* Involves manually testing parts of a code in an interactive environment. It complements formal testing frameworks and allows developers to be more innovative during development.
B. Why tests are important

	* Ensures code functions or software meets correct results or specifies requirements
	* Helps in early identification of bugs during development process
	* Ensures that new code changes do not break existing functionality as the codebase grows and evolves
	* Well-written documentation describing how the system is supposed to behave, makes the tests reliable for to new team members or wheb returning to old code.
	* Ensures that new features can be safely deployed to production frequently while ensuring functionality remains intact
	* Well-tested code helps mitigate the risks associated with deploying new sofware or changes to existing systems, reducing the chance of costly outages or data loss
C. How to write Docstrings to create tests

	* Docstrings are used to document python module, class, functions or methods of a code.
	* Docstrings must be defined with three `double-quotes`
	* No blank lines should be left before or after the docstring
	* The text starts in the next line after the opening quotes
	* The closing quotes have their own line
	* `Short summary` describing what function does must start with capital letter, end with a dot, and fit in a single line. It must start with an infinitive verb.
	* `Extended summary` provides details of what the function does. It should not go into details of the parameters. A blank line is left between the short summary and thr extended summary. Every paragraph ends with a dot.
	* `Parameter` section has the title 'Parameters' followed by a line with hyphen under each letter of the title. Parameters are identified by their name, followed by space, colon, space and the type(s)
	* Return will be defined in the same way as "Parameters"
	
D. What are the basic option flags to create tests

    Option flags provides flexible control on how test are run and how output is interpreted.
	1. Inline using doctest
	    a. ELLIPSIS (doctest.ELLIPSIS)
		- Allows the use of `...` in the expected output to signify any text
	    b. IGNORE_EXCEPTION_DETAIL (doctest.IGNORE_EXCEPTION_DETAIL)
		- Ignores the details of exceptions, such as error messages, and only checks for the type of exception
	    c. NORMALIZE_WHITESPACE (doctest.NORMALIZE_WHITESPACE)
		- Normalizes whitespace in both the expected and actual output before comparison. Useful when the output involves
		irregular whitespaces
	    d. ALLOW_UNICODE (doctest.ALLOW_UNICODE)
		- Treats Unicode and byte strings as equivalent in the output
	    e. SKIP (doctest.SKIP)
		- Excludes specific tests that are not relevant or cannot be run in the current environment
	    f. REPORT_ONLY_FIRST_FAILURE (doctest.REPORT_ONLY_FIRST_FAILURE)
		- Stops the test run on the 1st failure and reports only that failure. Useful for focusing on the initial issue wi		thout being overwhelmed by multiple failures
	    g. REPORT_NDIFF (doctest.REPORT_NDIFF)
		- Makes it easier to spot the difeferences between expected and actual output.

	Usage:
		`doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)`
		`python -m doctest -v my_script.py -o ELLIPSIS -o NORMALIZE_WHITESPACE`

	2. Command line
	    python -m unittest
	    -v, -b, -f, -c -k

E. How to find edge cases

	Finding edge case is essential in ensuring robustness and reliablity of a software. It is critical in understanding business rules and finding how the system interacts with external elements
	1. Understand the Requirements and Domain : For example, in a financial application, understand the limits on transaction amounts, currency formats, and decimal precision
	2. Analyze Input Space: Consider the data types, ranges, and possible formats of inputs.
	3. Think about the Extremes: 
	   * For numerical inputs, think about the minimum and maximum values.
	   * For collections (like lists, strings, arrays), consider empty collections, collections with one item, and very large collections.
	   * For strings, consider empty strings, strings of maximum length, and strings with special characters
	4. Consider Special Values and Limits: Identify special values that might have unique handling in your system, like None, 0, negative numbers, NaN, or Infinity.
	5. Review Business Rules and Constraints
	6. Inspect Algorithms and Logic: Consider conditions such as loops that might iterate zero times or exactly once, and recursive functions that might reach their base case immediately or after deep recursion.
	7. Use Boundary Value Analysis
	8. Consider External Interfaces and Integrations: Think about how your system interacts with external systems or components. Test scenarios like network failures, database connection loss, and timeouts.
	9. Think about Time and State
	10. Review Previous Bugs and Failures

**References**
- [Docstring Guide](https://pandas.pydata.org/docs/development/contributing_docstring.html)
- [Unit test in python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)
- [Unittest module](https://www.youtube.com/watch?v=6tNS--WetLI)

_"The only thing we have to fear is a lot of failure when running our unit test" - Frankline Roosevelt_
