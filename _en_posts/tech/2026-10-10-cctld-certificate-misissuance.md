---
title: "Breach of Country Domain Operators Leads to Unauthorized Google Certificates"
description: "How a breach of the operator of three countries' ccTLDs led to Google and YouTube certificates being issued, Chrome's block, and the limits of the padlock icon"
date: 2026-10-10
category: Tech
subcategory: News
tags: [tls-certificate, cctld, dns, chrome, web-pki]
image: /assets/og/en-2026-10-10-cctld-certificate-misissuance.png
---

After an outside company that operates the country domains of Ghana (.gh), Sierra Leone (.sl), and American Samoa (.as) was breached, attackers obtained valid HTTPS certificates for Google and YouTube domains. On October 6, 2026, the Google Chrome team disclosed what happened and said it had blocked the certificates in Chrome. Google's systems weren't breached, and Chrome users don't need to do anything.

![Google logo](/assets/images/tech/cctld-certificate-misissuance/01-logo-google.webp)
*Google logo*

## Timeline

![Timeline of the ccTLD hijacking and unauthorized certificate issuance](/assets/images/tech/cctld-certificate-misissuance/en/02-chart.webp)
*Timeline of the ccTLD hijacking and unauthorized certificate issuance — Source: self-rendered from the Google Chrome team and CT log lookups*

According to Google, the attackers took over the systems of an outside company managing the three country-code top-level domains (ccTLDs) and changed the authoritative DNS records of domains under them. With control of DNS, the attackers passed certificate authorities' (CA) domain ownership checks normally, and as a result certificates were issued for Google domains such as google.com.gh and youtube.sl.

- Country domains affected: .gh (Ghana), .sl (Sierra Leone), .as (American Samoa)
- What was breached: the third party responsible for operating the country domains; company name undisclosed
- Impact: several Google domains and other global brands and online services found in CT logs; names undisclosed
- Attacker: not identified

Google said there was no basis to consider the certificate authorities that issued the certificates at fault. The CAs simply followed the set procedures, with no way of knowing the DNS records had been changed.

## Preconditions for the attack

For this attack to work, the attackers had to be able to change the domains' DNS records. It didn't target personal PCs or browsers but took over a higher level of the internet's addressing system, so ordinary users had no way to block it.

| Item | This attack | Ordinary phishing |
| :--- | :--- | :--- |
| What was taken over | **Country domain operation** | A similar fake address |
| Address bar | The real domain | A different domain |
| Padlock icon | Shown normally | May be shown normally |
| User can tell | Practically impossible | Possible by checking the address |

Whether the certificates were actually used to attack users hasn't been disclosed. Fooling users with fake certificates requires redirecting their connections to the attacker's server, and while the attackers held DNS control, that was possible too.

## Issuances confirmed in CT logs

![Terminal screen querying youtube.sl certificates on Cert Spotter](/assets/images/tech/cctld-certificate-misissuance/en/03-term-ct.webp)
*Terminal screen querying youtube.sl certificates on Cert Spotter — Source: self-rendered from Cert Spotter CT log queries*

Every public HTTPS certificate is recorded in Certificate Transparency (CT) logs when issued. When I queried Cert Spotter directly on October 10, 2026, certificates issued by Let's Encrypt, not Google's own certificate authority, were recorded as below.

| Date | Domain | Issuing CA |
| :--- | :--- | :--- |
| September 22 | youtube.com.gh | Let's Encrypt |
| September 25 | google.sl (2) | Let's Encrypt |
| September 25 | youtube.sl (2) | **Let's Encrypt** |
| September 27 | youtube.as | Let's Encrypt |

The Hacker News reported that at least 12 certificates were issued in the names of Google and YouTube from September 22 to 27, 11 of them by Let's Encrypt and 1 by ZeroSSL. Because of query limits, I checked only some of the domains directly.

## Chrome's response and its limits

![Concept image of connections heading to another server after DNS records change](/assets/images/tech/cctld-certificate-misissuance/04-agy-dns.webp)
*Concept image of connections heading to another server after DNS records change — Source: concept image · self-generated with agy*

Chrome blocked the unauthorized certificates with CRLSet, its emergency block list, and revoked them together with the issuing authorities so that programs outside Chrome are also protected. It said it also preemptively blocked certificates for other organizations found in CT logs and notified the organizations it could reach.

Google also noted two limits: it can't be sure its analysis identified every affected domain, and Chrome's measures don't reliably protect users of browsers other than Chrome. That's why it recommended that domain owners monitor directly rather than relying only on browser-side blocks.

In the long run, Google is pushing at the CA/Browser Forum to shorten certificate validity periods and the period for reusing domain validation results.

## What domain operators should do

![Domain operator action summary card](/assets/images/tech/cctld-certificate-misissuance/en/05-items.webp)
*Domain operator action summary card — Source: self-rendered from the Google Chrome team's recommendations*

The first measure Google recommended is monitoring CT logs. It advised regularly checking issuance records, including domains that are registered but unused and regional country domains, and said organizations with .gh, .sl, or .as domains should start with recent issuances.

The second is setting strict CAA records (DNS records that list the permitted certificate authorities). CAA can't block issuance while DNS is taken over, but CAs can reuse a completed domain validation result for a certain period; after regaining control, restricting issuance to a specific ACME account and validation method (RFC 8657) can stop attackers from reusing earlier validation results to get certificates issued again. You also need to check whether your CA supports such account and validation method restrictions.

If you've already found a certificate you don't recognize, the next step is to immediately ask the issuing CA to revoke it. CT log records include the issuer's name, so you know right away whom to contact.

![Korea Internet & Security Agency logo](/assets/images/tech/cctld-certificate-misissuance/06-logo-kisa.webp)
*Korea Internet & Security Agency logo*

Korea's .kr and .한국 domains are managed by the Korea Internet & Security Agency (KISA). No harm in Korea related to this incident has been reported, but Korean companies that also run overseas regional domains can check CT logs the same way.

## Sources

- [[Google] Chrome's response to recent ccTLD registry hijacks: what happened, CRLSet, recommendations (2026-10-06)](https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/)
- [[Boan News] Breach of country domain operator and unauthorized Google certificates (2026-10-08)](https://www.boannews.com/news/articleView.html?idxno=146250)
- [[The Hacker News] 12 certificates, issuance period, counts by CA (2026-10)](https://thehackernews.com/2026/10/attackers-hijack-gh-sl-and-as.html)
- [[BleepingComputer] ccTLD registry breach and Google domain hijacking (2026-10)](https://www.bleepingcomputer.com/news/security/hackers-hijack-google-domains-after-breaching-cctld-registries/)
- [[Cert Spotter] CT log issuance lookup API (queried 2026-10-10)](https://api.certspotter.com/v1/issuances)
- [[IETF] RFC 8657, account and validation method restrictions for CAA records](https://www.rfc-editor.org/rfc/rfc8657)
