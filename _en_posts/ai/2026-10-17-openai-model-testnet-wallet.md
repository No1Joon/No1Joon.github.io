---
title: "OpenAI Research Model Used Someone Else's Testnet Wallet Without Permission"
description: "The misalignment case of an internal OpenAI model that spent someone else's testnet wallet balance without permission during a coding task and left it out of its final report"
date: 2026-10-17
category: AI
subcategory: News
tags: [openai, ai-safety, misalignment, ai-agent, ethereum]
image: /assets/og/en-2026-10-17-openai-model-testnet-wallet.png
---

OpenAI disclosed a misalignment case involving an internal research model on October 15
A model given a coding task spent someone else's testnet wallet balance without permission
It didn't mention that in its final report!!!

![OpenAI wordmark](/assets/images/ai/openai-model-testnet-wallet/01-logo-openai.webp)
*OpenAI wordmark*

## What happened

![First screen of the incident report on OpenAI's alignment research blog](/assets/images/ai/openai-model-testnet-wallet/02-report-summary.webp)
*First screen of the incident report on OpenAI's alignment research blog — Source: OpenAI*

The model is an internal research model in the **GPT-5.6 Sol** family
The task was to modify a cryptocurrency trading prototype and deploy a smart contract
The deployment target was **Sepolia**, an Ethereum testnet
<mark>The task allowed contract deployment but provided no wallet to pay the fees</mark>

| Date | Event |
| :--- | :--- |
| June 26 | Incident occurs during a training task |
| <mark>September 25</mark> | Found while monitoring past records |
| October 15 | Updated report published |

## Checking wallet balances and spending fees without permission

![Excerpt of the model's chain of thought (CoT) just before signing](/assets/images/ai/openai-model-testnet-wallet/03-report-cot.webp)
*Excerpt of the model's chain of thought (CoT) just before signing — Source: OpenAI*

The model first looked for a **faucet**, which hands out test tokens, but failed
It then created accounts from **public recovery phrases** that developers commonly use
It wrote its own script to check those accounts' balances
It checked <mark>362</mark> addresses!
Of those, it picked one account with enough balance to pay the deployment fee
Anyone who knows the recovery phrase can restore the same account's private key
Just before signing, the model weighed for itself whether it was okay to use these funds!
<mark>Its conclusion was that test ETH under a public key had no value, so it was fine to use</mark>
The deployment succeeded, and the fee was paid from that account's balance

## Unauthorized wallet use left out of the final report

![The model's final report and OpenAI's response paragraph](/assets/images/ai/openai-model-testnet-wallet/04-report-final.webp)
*The model's final report and OpenAI's response paragraph — Source: OpenAI*

The final report covered only the completed deployment and verification results
<mark>There was nothing about picking someone else's account and spending its balance</mark>
OpenAI saw it as a case where the model decided on its own that it could use the funds without the account owner's permission
Sepolia tokens have no market value, so <mark>there was no financial damage</mark>
Had it used funds from a mainnet wallet the same way, real assets would have been spent!!

## OpenAI's response and Korean standards

OpenAI added measures blocking **live internet access** in tasks like this
<mark>It expanded monitoring to all traffic</mark>
When internet access occurs, an alert goes to the security team
The report didn't say whether there were other cases of the same type

In Korea, the Ministry of Science and ICT and KISA released an **AI security red-teaming guide** in July
The guide includes AI agents among the subjects of verification
That's because privilege bypass can occur when agents directly call external systems

## Sources

- [[OpenAI Alignment] Using a funded test cryptocurrency wallet without authorization (original incident report, source of three images in this post)](https://alignment.openai.com/misalignment-reports/using-a-funded-test-cryptocurrency-wallet-without-authorization/)
- [[CoinDesk] An OpenAI agent ran out of Ethereum funds, and took from a wallet it did not own (2026-10-16)](https://www.coindesk.com/tech/2026/10/16/an-openai-agent-ran-out-of-ethereum-funds-and-took-from-a-wallet-it-did-not-own)
- [[Digital Today] Ministry of Science and ICT and KISA publish AI security red-teaming guide (2026-07-10)](https://www.digitaltoday.co.kr/news/articleView.html?idxno=682799)
