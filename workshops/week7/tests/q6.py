OK_FORMAT = True  # This tells otter-grader the file is in OK format

test = {
  'name': 'Question 6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check minimum and maximum steps 
          >>> bool((minSteps == 0.9101380609604088) or (minSteps == np.float64(0.9101380609604088)))
          True
          >>> bool((maxSteps == 62486.690753464914) or (maxSteps == np.float64(62486.690753464914)))
          True
          >>> bool((meanSteps ==  6985.685884992229) or (meanSteps == np.float64(6985.685884992229)))
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}