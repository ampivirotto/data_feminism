OK_FORMAT = True  # This tells otter-grader the file is in OK format

test = {
  'name': 'Question 8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check minimum, maximum, and mean sleep hours
          >>> bool((minSleep == -0.1944527906201543) or (minSleep == np.float64(-0.1944527906201543)))
          True
          >>> bool((maxSleep == 12.140232872862926) or (maxSleep == np.float64(12.140232872862926)))
          True
          >>> bool((meanSleep ==  6.505462918406444) or (meanSleep == np.float64(6.505462918406444)))
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