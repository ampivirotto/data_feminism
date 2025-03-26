Questions:

1.  In our data cleaning exercise, you selected a variable to examine
    and clean. What column did you choose, and what specific issues did
    you identify? What decisions did you make about how to clean the
    data, and why? Did you encounter any ethical considerations in this
    process---such as deciding what counted as an error, what to remove,
    or how to interpret missing data? Did the exercise raise any
    questions for you about how the data was originally collected?

2.  One goal of data cleaning is to make data more \'usable,\' but who
    decides what is usable? In disability data collection and beyond,
    standardization and classification choices can impact the visibility
    and agency of marginalized groups. Missing or incomplete data is
    often seen as a problem to fix, yet Data Feminism suggests that
    these gaps can reveal whose voices have been excluded. How can
    researchers balance the need for structured, analyzable data with
    the responsibility to respect self-identification, lived
    experiences, and the insights that missing data might reveal?

3.  From "Bias in artificial intelligence algorithms and recommendations
    for mitigation" by Nazer et al. (2023):

> Preprocessing of the data refers to transforming patient-related raw
> data to a readable and structured digitized format that is ready for
> analysis. It involves analytical data manipulations such as
> imputations of missing values, selecting highly predictive variables,
> and aggregation
> \[[19](https://pmc.ncbi.nlm.nih.gov/articles/PMC10287014/#pdig.0000278.ref019)\].
> It is crucial to ensure that these techniques account for factors that
> may contribute to bias and health disparities in the developed
> algorithms.
>
> Aggregation may result in bias when a "one-size-fits-all" model is
> used for groups with different conditional distributions
> \[[33](https://pmc.ncbi.nlm.nih.gov/articles/PMC10287014/#pdig.0000278.ref033)\].
> Hispanics, for example, tend to have higher rates of diabetes and
> diabetes-related complications compared to Whites
> \[[34](https://pmc.ncbi.nlm.nih.gov/articles/PMC10287014/#pdig.0000278.ref034)\].
> Using AI-based algorithms may help diagnose and monitor diabetes in
> Hispanic populations; however, it can also lead to aggregation bias if
> the models are not sensitive to the fact that there are varying
> Hispanic ethnic groups (e.g., Mexicans, Puerto Ricans). If these
> issues are left unaddressed during this stage, the algorithm would be
> developed with biased data and will either have an overall poor
> performance or perform properly solely for the majority of the
> represented population.
>
> Managing missing data and outliers is another challenging aspect
> during this stage. The most common approaches used to address this are
> complete case analysis or mean imputation
> \[[35](https://pmc.ncbi.nlm.nih.gov/articles/PMC10287014/#pdig.0000278.ref035)\].
> With such approaches, patients with values that are missing or
> outliers on any of the variables are deleted from the analysis
> (complete case analysis) or their values are replaced by mean
> estimates based on the remaining data (mean imputation). Though this
> would facilitate the process of analyzing the data, it does not
> acknowledge the fact that such findings may reflect the diversity of
> patients. For example, weight may not be available in patients with
> disabilities and wheelchair users. Similarly, extreme values of
> weights may be seen more commonly in certain patient populations such
> as obesity among Black patients and lower weights in patients with
> limb amputation or terminal illnesses.
>
> During this stage, the features/variables that are selected for
> incorporation in the model may also be a source of bias. An example
> for this type of bias may be encountered with prediction algorithms
> designed for the early screening of sepsis. The Surviving Sepsis
> Campaign guidelines recommend the use of machine learning algorithms
> that utilize scoring systems for the early screening of patients
> \[[36](https://pmc.ncbi.nlm.nih.gov/articles/PMC10287014/#pdig.0000278.ref036)\].
> Since the Sequential Organ Failure Assessment (SOFA) score is
> recommended in the guidelines, it is very likely that algorithms would
> incorporate this score as one of the features/variables. However,
> several studies have demonstrated suboptimal performance of the SOFA
> score among various patient populations such as Black patients, female
> patients, and patients with disabilities
> \[[37](https://pmc.ncbi.nlm.nih.gov/articles/PMC10287014/#pdig.0000278.ref037)--[40](https://pmc.ncbi.nlm.nih.gov/articles/PMC10287014/#pdig.0000278.ref040)\].
> Such findings suggest potential health disparities when utilizing
> AI-based algorithms that incorporate the SOFA score to guide clinical
> decision-making and triage of certain patient populations with
> suspected sepsis.

Beyond reformatting qualitative data, data cleaning can also involve
removing outliers in quantitative datasets. This practice is routine,
yet it can be particularly harmful if it disproportionately removes data
points from marginalized groups, skewing results toward the majority. If
you were consulting with a biostatistician concerned about this issue,
what questions would you ask to assess whether outlier removal might
introduce bias? What strategies could you suggest ensuring that
statistical rigor is maintained without reinforcing systemic exclusion?

Pick one of the following discussion questions:

1.  How can the collection of demographic disability data, as discussed
    in Why Collect Demographic Disability Data, help address systemic
    healthcare disparities, and what challenges might arise in ensuring
    this data is both inclusive and effectively used for policy-making?

2.  If classifications (such as gender and disability) are shaped by
    power structures, what happens when marginalized groups reject
    categorization altogether? Could refusing to be counted (\"right to
    opacity\") ever be a form of resistance, or does it risk reinforcing
    invisibility and exclusion?

3.  It is believed that all data collection requires categorization to
    be actionable. If we were to radically rethink classification, could
    a world exist where demographic categories are fluid, self-defined,
    and constantly evolving? What might that system look like, and how
    would it balance the flexibility and the practical needs of
    governance, healthcare, and advocacy? Is it possible to make
    uncategorized data actionable?

4.  Chapter 4 discusses how missing data of marginalized groups can also
    sometimes keep them protected. It explains it as the paradox of
    exposure, \"the double bind that places those who stand to
    significantly gain from being counted in the most danger from that
    same counting (or classifying) act.\" How do we mitigate this risk
    and how can we work towards responsibly acquiring data from
    marginalized communities who may be fearful of losing the
    invisibility that kept them protected?

5.  Both readings highlight how classification systems---whether in
    disability data collection or gender identity---can either empower
    or oppress marginalized groups. What are the ethical challenges of
    collecting demographic data on vulnerable populations, and how can
    researchers and policymakers ensure that data collection promotes
    equity rather than reinforcing systemic discrimination?

6.  Chapter 4 of Data Feminism discusses the "paradox of exposure," the
    truth that the people who would benefit the most from being counted
    are also those harmed by being made visible. How does this concept
    relate to the idea of the privilege hazard? And how do these two
    concepts interact in the process of data collection?

7.  Both readings discuss the risks of exclusion from data systems, but
    what if data collection was built around active consent rather than
    automatic inclusion? How would this shift the power between
    individuals and data collectors, and what implications would this
    have for policymaking and resource distribution?

8.  How could disability data hinder one\'s access to proper healthcare
    by creating preconceived biases about people\'s conditions while
    also making their healthcare more comprehensive? Why is it important
    that we create a more nuanced definition of disability when
    measuring it and how can we make it more inclusive for individuals
    who may not have the means to get a legal diagnosis for their
    disability?

9.  How can data classification systems, like those discussed in What
    Gets Counted Counts, be redesigned to be both inclusive and
    effective for policy-making? Considering the statement, \"What is
    counted---like being a man or a woman---often becomes the basis for
    policymaking and resource allocation,\" how can we ensure that
    marginalized identities are recognized without compromising data
    usability?

10. \"What gets counted counts" is a central theme in both readings,
    highlighting how classification systems shape visibility, access,
    and policy decisions. How do the current limitations in disability
    demographic data parallel the exclusion of nonbinary identities in
    gender classification, and what steps can be taken to create more
    inclusive and equitable data systems?

11. What aspects of identity, experience, and oppression is more
    qualitative than quantitative, and what happens when we try to force
    them into structured categories? How can data systems acknowledge
    the fluid and unquantifiable aspects of lived experiences without
    erasing them for categorization purposes?

12. The lack of demographic disability data contributes to the belief
    that disability inevitably leads to poorer health outcomes. Due to
    the absence of data, blame is placed on the disabilities of
    individuals, rather than on the failures of the health system to
    offer equitable care. In what way does this system end up
    reinforcing harmful perceptions of disability? What are some ways in
    which data collection can effectively work towards addressing these
    issues, while also ensuring that more harm is not done?
