# Tino: Context-Aware NLP for Brazilian Learners of English

**Applied AI · Natural Language Processing · Sociolinguistics · Python**

Tino turns a linguistic question into an interactive product: **How can feedback help a learner adapt English to an audience without treating their first language as a defect?**

The project connects linguistic problem framing with an LLM-backed API and a bilingual web interface. Its focus is register calibration, not blanket grammar correction. The reviewed implementation is a prototype, not a benchmarked language-assessment system.

[Source repository](https://github.com/Gutembergfox/tino) · [Documented demo](https://tino-deploy.vercel.app)

## The problem

Brazilian learners may need to move between academic writing, workplace communication, and casual conversation. A form that works in one situation can be distracting in another. Feedback should therefore explain the relationship between language, audience, and purpose, rather than simply label a phrase “wrong.”

Tino's project rationale draws on register, audience design, and cross-linguistic influence. It asks the model to distinguish conversational features from possible Brazilian Portuguese transfer, while treating transfer explanations as hypotheses rather than proven causes. [Project rationale](https://github.com/Gutembergfox/tino/blob/60c393abb74715923de9a34593ccbd430e318494/about.html)

## The implemented approach

1. **Make context explicit.** The user submits 50–500 words of English and selects academic, professional, or casual register.
2. **Apply a domain-specific instruction set.** A FastAPI endpoint combines the declared context and learner text with sociolinguistic instructions. The prompt includes discourse markers, false cognates, and possible Portuguese calques.
3. **Request a structured analysis.** The OpenAI Responses API is called with JSON-object output enabled. The code configures the model identifier `gpt-5.6`; this records the repository configuration, not independently verified model availability.
4. **Explain individual passages.** The requested output includes the original quote, issue, register interpretation, transfer hypothesis, contextual explanation, and suggested alternative.
5. **Present feedback progressively.** The browser displays an overall assessment, annotation cards, and recurring patterns. PT/EN interface controls and a separate translation endpoint support English versions of the explanatory fields.

The repository also implements a separate `/analyze-pt` endpoint for Brazilian Portuguese register analysis, accepting 1–500 words. Its prompt includes cautious references to linguistic change. The inspected main interface submits to the English-analysis route, so the Portuguese endpoint should not be presented as a fully integrated input-language selector. [Backend](https://github.com/Gutembergfox/tino/blob/60c393abb74715923de9a34593ccbd430e318494/main.py) · [Interface](https://github.com/Gutembergfox/tino/blob/60c393abb74715923de9a34593ccbd430e318494/index.html)

## Observed stack and engineering choices

- **Backend:** Python, FastAPI, Pydantic request models, OpenAI Python SDK, and python-dotenv; Uvicorn is listed for local serving.
- **Frontend:** HTML, JavaScript, and Tailwind CSS loaded from a CDN.
- **Deployment configuration:** Vercel serverless entry point and routing configuration.
- **User experience:** word-count checks, loading and error states, annotation rendering using `textContent`, and a copyable software citation.
- **PWA scaffolding:** web manifest and versioned service-worker caching for the application shell. Model analysis still requires a network connection.
- **Application data flow:** no database or application-level persistence of learner submissions is implemented in the inspected code. Submitted text is sent to the model provider; this is not an end-to-end data-retention or privacy guarantee.

[Dependencies](https://github.com/Gutembergfox/tino/blob/60c393abb74715923de9a34593ccbd430e318494/requirements.txt) · [Deployment entry point](https://github.com/Gutembergfox/tino/blob/60c393abb74715923de9a34593ccbd430e318494/api/index.py) · [Routing](https://github.com/Gutembergfox/tino/blob/60c393abb74715923de9a34593ccbd430e318494/vercel.json) · [Service worker](https://github.com/Gutembergfox/tino/blob/60c393abb74715923de9a34593ccbd430e318494/service-worker.js)

## Illustrative walkthrough, not a measured result

Consider this synthetic excerpt within a longer academic paragraph:

> “Like, the students have more access to information now.”

An illustrative annotation could explain that sentence-initial “Like” functions as a conversational filler, propose a possible connection with Portuguese “tipo,” and suggest:

> “Students now have greater access to information.”

This is an editorial illustration of the intended feedback, not captured model output or evidence of accuracy. The excerpt alone is below the endpoint's 50-word minimum. The same form may be appropriate in casual conversation, and its presence does not establish Portuguese transfer.

## What has been verified, and what has not

The source contains a controlled English sample in `test_tino.py`, instructions for a model smoke test, and an implemented request-to-report path. The smoke-test script sends the sample to Chat Completions and attempts to parse the response as JSON.

Its current scope is narrower than the README suggests: **it does not assert required output fields, annotation quality, or linguistic correctness**, and it prints JSON-parsing errors rather than enforcing a failing test result. It also uses a different API path from the application, which calls Responses.

This case study is based on source inspection, not a new live model run. No benchmark dataset, human-rating study, measured learning benefit, accuracy score, or latency/cost result was established. The documented demo URL could not be checked successfully through the research tool during this review; no availability claim is made. [Smoke-test source](https://github.com/Gutembergfox/tino/blob/60c393abb74715923de9a34593ccbd430e318494/test_tino.py) · [Testing documentation](https://github.com/Gutembergfox/tino/blob/60c393abb74715923de9a34593ccbd430e318494/docs/TESTING.md)

## Limitations and proposed next steps

These are proposed improvements, not shipped features or commitments.

- **Validate the full response contract.** Parsing currently establishes a JSON object, not conformity to a complete annotation schema. Add typed output validation and explicit checks that quoted spans occur in the input.
- **Build an evaluation set.** Include acceptable informal language, formal texts needing no intervention, ambiguous false cognates, and plausible non-transfer explanations.
- **Measure feedback quality.** Have qualified reviewers assess register appropriateness, rewrite fidelity, unsupported transfer claims, and overcorrection. Report disagreement and uncertainty.
- **Test the actual application path.** Add mocked endpoint tests, input-boundary cases, malformed provider outputs, translation invariants, and bilingual UI behavior.
- **Strengthen operational readiness.** Review dependency versioning, rate limiting, cost controls, request handling, and user-facing data-use information before broader use.

## Why this belongs in a Data Science + Linguistics portfolio

Tino demonstrates a concrete bridge between domain knowledge and applied NLP: defining a context-sensitive task, expressing linguistic criteria in an explicit prompt and response contract, and exposing the resulting analysis through a usable interface.

The demonstrated outcome is an inspectable prototype and product workflow. Model training, predictive performance, production scale, client adoption, and educational efficacy are not claimed. The README explicitly credits Codex as a development collaborator, which should be retained as part of transparent project attribution.

**Review basis:** public `main` snapshot `60c393abb74715923de9a34593ccbd430e318494`, inspected on 21 October 2026. Evidence links are pinned to that snapshot so implementation claims remain auditable.


[Back to portfolio showcase](README.md)
