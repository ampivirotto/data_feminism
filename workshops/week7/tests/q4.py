OK_FORMAT = True  # This tells otter-grader the file is in OK format

test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check minimum and maximum blood oxygen level  
          >>> bool((minBloodO2 == 90.79120814564097) or (minBloodO2 == np.float64(90.79120814564097)))
          True
          >>> bool((maxBloodO2 == 100.0) or (maxBloodO2 == np.float64(100.0)))
          True
          >>> bool((meanBloodO2 == 97.84158102099076) or (meanBloodO2 == np.float64(97.84158102099076)))
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