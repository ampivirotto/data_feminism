OK_FORMAT = True  # This tells otter-grader the file is in OK format

test = {
  'name': 'Question 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Set your two variables to the maximum and minimum values of heart rate
          >>> bool((minimumHeartRate == 40.0) or (minimumHeartRate == np.float64(40)))
          True
          >>> bool((maximumHeartRate == 296.5939695131042) or (maximumHeartRate == np.float64(296.5939695131042)))
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