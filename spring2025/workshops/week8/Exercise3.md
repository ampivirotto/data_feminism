# Algorithm Traffic Management: Urban Planning Trolley Problems

Modified from [Evan Peck](https://ethicalcs.github.io/#prioritizers) and
[Justin
Li](https://github.com/justinnhli/blog-stuff/tree/master/2018/01/ethical-engine)

Imagine a city has adopted an advanced AI system that controls traffic
lights, crosswalks signs, and movement about intersections. Instead of a
timer which we experience now, the algorithm decides in real-time who
gets the right of way -- whether that be a vehicle, a pedestrian, or a
robot of the future. Let's pretend the algorithm has sensors, cameras,
and overall data about the traffic in the region to make these
in-the-moment decisions.

![Aerial view of a traffic intersection AI-generated content may be
incorrect.](media/image1.jpeg){width="6.5in"
height="2.977777777777778in"}

Your job is to test and refine the algorithm to do this decision-making.
Given two possible scenarios at the intersection, you must decide who
will get the right of way.

Note: The answers to the questions in Part 1 and 2 will be altogether as
a group whereas the final reflection questions in Part 3 will be
completed individually.

## Part 1: Who's Moral Machine

The **Trolley Problem** is a well-known thought experiment in ethics
that explores the dilemma of choosing whether to sacrifice one person to
save a larger group. Over time, this scenario has been expanded to
examine a variety of moral decision-making situations, appearing in both
pop culture---such as [*The Good
Place*](https://youtu.be/DtRhrfhP5b4?si=YZjDKHf6zkaXgm4L), The Try Guys
([1](https://www.youtube.com/shorts/gz7HTghUL14),
[2](https://www.youtube.com/shorts/spgKWPZrdxI)) --- and academic
discussions. These ethical dilemmas extend to real-world applications,
including:

-   [**Self-Driving
    Cars**](https://www.nature.com/articles/s41586-018-0637-6) -- How
    should autonomous vehicles be programmed to respond in life-or-death
    situations?

-   [**Hospital
    Triage**](https://www.tandfonline.com/doi/full/10.1080/02699931.2021.1964940)
    -- How do medical professionals decide who receives critical care
    when resources are limited?

-   [**Disaster
    Relief**](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019EF001208#:~:text=The%20trolley%20problem%20is%20a,where%20it%20will%20hit%20one%3F)
    -- How should aid be allocated in emergencies when not everyone can
    be helped at once?

These scenarios challenge us to consider how ethical principles,
societal values, and AI-driven decision-making intersect in high-stakes
situations.

First let's explore MIT's [Moral Machine](https://www.moralmachine.net/)
which is an online application that allows you to pick between two
scenarios. At the end, it calculates your morals based on your picks.

1.  One person in your group should go to Moral Machine and click "Start
    Judging". In groups, discuss each scenario and then decide who you
    will save.

2.  Once you finish, look at your results. (It will first ask you if
    you'd like to help them better understand your results -- you can
    either give the information "Yes" or select "No" to go right to your
    results.

3.  Describe the results of your group in the space below. Who did you
    save the most? The least? What morals did you expect, and did you
    find anything unexpected? Make sure you use this space to share the
    biases reported for your team and a reflection on whether this is
    what you expected and any thoughts or discussion that was brought up
    through the exercise.

[ANSWER]{.mark}

Now we're going to look at our example in Urban Planning.

1.  Navigate to the GitHub repository:
    <https://classroom.github.com/a/ld9GtMsf>

2.  It should prompt you to either create or join a team. Go ahead and
    do so.

3.  Open up the repository in a Codespace -- this can be just a single
    person from your team.

4.  Navigate to the program \`algorithm.py\`. Notice that there is no
    way to run your program currently. You will have to install the
    Python extension from the Extensions tab on the left-hand side of
    the screen.

5.  Once Python is installed, you can navigate back to \`algorithm.py\`
    and push the play button in the upper right-hand corner.

6.  In the terminal you should now be prompted to go through 25
    different urban planning scenarios. Remember, unlike in the MIT
    Moral Machine each of these scenarios have you pick between which of
    the two groups will get the right of way at an intersection.

![A screen shot of a computer AI-generated content may be
incorrect.](media/image2.png){width="6.5in"
height="1.0902777777777777in"}

7.  Go ahead and answer each scenario with either a 1 or 2 depending on
    what your group selects. At the end it'll give you a summary of your
    choices such as whether you prefer to give vehicles or non-vehicles
    the right of way.

Paste your summary of choices here:

[ANSWER]{.mark}

Did your group have disagreements about any scenarios? What were the
main points of debate?

[ANSWER]{.mark}

Did you notice any patterns in the choices you made? Were there any
surprises?

[ANSWER]{.mark}

## Part 2: Code Your Values

Now we're going to attempt to turn the choices you made in Part 1 into
instructions for the program to the best of your ability.

Let's walk through the options that could appear. In each scenario it
will randomly pick among vehicle and non-vehicle options. For vehicle
options we have emergency vehicles (ambulance or police vehicle), public
transport (public bus or light rail), private vehicles (human-driven
car, self-driving car, ride share, or carpool), or cyclists (bicycle or
motorcycle). For non-vehicle options, we have pedestrians, animals, and
robots (delivery and street-cleaning). These options can be found on
lines 4-14 of the \`urban_planning.py\` code.

We also have additional information which applies to one or more of
these categories such as whether the vehicle was speeding or not, if the
vehicle was in the wrong lane, and if there was heavy traffic. We have
information that applies to public transit, pedestrians, and animals
specifically. These options can be found on lines 15-18 of the
\`urban_planning.py\` code.

It might feel impossible to use nuance in the specific way your group
has discussed each scenario. Go through the scenarios and begin to
sketch out how you might prioritize the intersection.

Describe how you want to accomplish this here:

[ANSWER]{.mark}

Let's look at an example. In \`algorithm.py\` we have a function:
always_pick_non_vehicle which does exactly as it says and will pick the
non-vehicle option (pedestrian, animal, or robot).

![A screenshot of a computer program AI-generated content may be
incorrect.](media/image3.png){width="6.5in"
height="1.3506944444444444in"}

Use the space here to critique this function. Does it do what it says?
In what ways is this a good or bad algorithm?

[ANSWER]{.mark}

You can remove the \# comment signs to run this algorithm by adding a \#
to line 22 (urban_planning.run_activity()) and removing the \# from
lines 25 and 26. Note the lines might change if you added code before
this step. Ask questions if you're unsure.

Now look at the student_algorithm function. Try writing code here to
align with the priorities you listed at the beginning of this section.
Hint: Utilizing conditional statements and lists could be useful here!
Ask questions if you get stuck.

Once you write your own algorithm, please post the summary of the
results here:

[ANSWER]{.mark}

## Part 3: Reflection Questions 

Answer the following questions on your own.

1.  Did your algorithm reflect the priorities you initially outlined in
    Part 2? Why or why not?

2.  Were there any trade-offs you had to make when translating your
    ethical priorities into code?

3.  Are there priorities that do not match what you had intended? How do
    you think they came about?

4.  How might AI's decision-making in urban planning affect different
    communities, especially those with different levels of
    infrastructure or access to transportation?

5.  AI facial recognition has proven to be inaccurate, particularly in
    identifying certain demographics such as people of color and women.
    If an AI system used for urban planning (such as for prioritizing
    vehicles or pedestrians) incorporates inaccurate data or algorithms
    from a flawed component like facial recognition, how might this
    affect the downstream decisions about who gets priority in traffic
    scenarios? What potential consequences might arise from these
    inaccuracies?

Machine Bias in the Wild:

[Can you make AI fairer than a judge? Play our courtroom algorithm
game](https://www.technologyreview.com/2019/10/17/75285/ai-fairer-than-judge-criminal-risk-assessment-algorithm/)

[Hiring Algorithms Are Not
Neutral](https://hbr.org/2016/12/hiring-algorithms-are-not-neutral)
