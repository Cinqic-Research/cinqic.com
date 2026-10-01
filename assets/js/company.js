(function () {
  "use strict";

  window.CINQIC = {
    name: "Cinqic",
    founder: "Markus Gillyard",
    launchDate: "2026-08-02",
    launchState: "launched",
    mission:
      "Build helpful open-source software that helps people learn, create, think clearly, and solve problems while respecting users’ privacy and ownership.",
    vision: "Create accessible, useful, and modifiable software while keeping AI a choice.",
    projects: {
      juniper: {
        name: "Juniper",
        category: "app",
        status: "Published prerelease",
        publishedVersion: "0.3.0-rc.33",
        repository: "https://github.com/Cinqic-Research/Juniper-App",
        release: "https://github.com/Cinqic-Research/Juniper-App/releases/tag/v0.3.0-rc.33",
      },
      calculator: {
        name: "Cinqic Calculator",
        category: "app",
        status: "Released",
        windowsVersion: "1.1.0",
        linuxVersion: "1.1.0",
        androidVersion: "1.1.0",
        repository: "https://github.com/Cinqic-Research/Cinqic-Calculator",
      },
      aaa: {
        name: "AAA",
        category: "research",
        status: "Active experimental research; current phase aaa.python.v1",
        repository: "https://github.com/Cinqic-Research/AAA",
      },
      juniperLM1: {
        name: "Juniper LM 1",
        category: "research",
        status: "Active research, conversational-first; no checkpoint trained or released",
        repository: "https://github.com/Cinqic-Research/Juniper-LM-1",
      },
      juniperEncoder: {
        name: "Juniper Encoder",
        category: "completed research",
        status: "Retired 2026-09-15; research complete, no model released",
        repository: "https://github.com/Cinqic/Juniper-Encoder",
      },
      juniperMath1: {
        name: "Juniper Math 1",
        category: "completed research",
        status: "Research complete; no approved Phase 8 release",
        repository: "https://github.com/Cinqic/juniper-math-1",
      },
    },
  };

  window.CINQIC.companyCopy = function () {
    return window.CINQIC.launchState === "launched"
      ? "Cinqic officially launched August 2, 2026."
      : "Cinqic is launching August 2, 2026.";
  };
}());
