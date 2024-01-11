# Break lines according to Unicode rules
%bcond_without perl_Test2_Suite_enables_unicode

Name:           perl-Test2-Suite
Version:        0.000111
Release:        1%{?dist}
Summary:        Set of tools built upon the Test2 framework
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test2-Suite/
Source0:        http://www.cpan.org/authors/id/E/EX/EXODIST/Test2-Suite-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Importer) >= 0.024
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Pluggable) >= 2.7
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Sub::Info) >= 0.002
BuildRequires:  perl(Term::Table) >= 0.002
BuildRequires:  perl(Term::Table::Cell)
BuildRequires:  perl(Term::Table::LineBreak)
BuildRequires:  perl(Term::Table::Util)
# Test2::API version from Test2 in META
BuildRequires:  perl(Test2::API) >= 1.302127
BuildRequires:  perl(Test2::API::Context)
BuildRequires:  perl(Test2::Event)
BuildRequires:  perl(Test2::Event::Exception)
# Test2::Event::Note loaded by send_event()
BuildRequires:  perl(Test2::Event::Note)
# Test2::Event::Skip loaded by send_event()
BuildRequires:  perl(Test2::Event::Skip)
BuildRequires:  perl(Test2::EventFacet)
BuildRequires:  perl(Test2::Hub::Interceptor)
BuildRequires:  perl(Test2::Hub::Subtest)
BuildRequires:  perl(Test2::IPC)
BuildRequires:  perl(Test2::Tools::Tiny)
BuildRequires:  perl(Test2::Util)
BuildRequires:  perl(Test2::Util::HashBase)
BuildRequires:  perl(Test2::Util::Trace)
BuildRequires:  perl(threads)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Optional run-time:
# Sub::Util or Sub::Name
BuildRequires:  perl(Sub::Util)
%if %{with perl_Test2_Suite_enables_unicode}
BuildRequires:  perl(Unicode::GCString)
%endif
# Tests:
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(Test2::EventFacet::Assert)
BuildRequires:  perl(Test2::Formatter::TAP)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(Data::Dumper)
Requires:       perl(Importer) >= 0.024
Requires:       perl(Module::Pluggable) >= 2.7
Requires:       perl(Sub::Info) >= 0.002
# Sub::Util or Sub::Name
Suggests:       perl(Sub::Util)
Requires:       perl(Term::Table) >= 0.002
# Test2 not used in any useful way
# Test2::API version from Test2 in META
Requires:       perl(Test2::API) >= 1.302127
Requires:       perl(Test2::Event)
# Test2::Event::Note loaded by send_event()
Requires:       perl(Test2::Event::Note)
# Test2::Event::Skip loaded by send_event()
Requires:       perl(Test2::Event::Skip)
Requires:       perl(Test2::EventFacet)
Requires:       perl(threads)
Requires:       perl(utf8)
%if %{with perl_Test2_Suite_enables_unicode}
# Unicode::GCString for formating double-width strings
Recommends:     perl(Unicode::GCString)
%endif
# perl-Test2-AsyncSubtest-0:0.000020-1.fc28 merged
Provides:       perl-Test2-AsyncSubtest = %{version}-%{release}
Obsoletes:      perl-Test2-AsyncSubtest < 0.000020-2
# perl-Test2-Workflow-0:0.000018-4.fc27 merged
Provides:       perl-Test2-Workflow = %{version}-%{release}
Obsoletes:      perl-Test2-Workflow < 0.000018-5

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Importer|Module::Pluggable|Sub::Info|Term::Table|Test2::API)\\)$

%description
Rich set of tools, plugins, bundles, etc. built upon the Test2 testing
library. If you are interested in writing Perl tests this is the distribution
for you.

%prep
%setup -q -n Test2-Suite-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Mar 15 2018 Petr Pisar <ppisar@redhat.com> - 0.000111-1
- 0.000111 bump

* Mon Mar 12 2018 Petr Pisar <ppisar@redhat.com> - 0.000108-1
- 0.000108 bump

* Wed Mar 07 2018 Petr Pisar <ppisar@redhat.com> - 0.000106-1
- 0.000106 bump

* Tue Mar 06 2018 Petr Pisar <ppisar@redhat.com> - 0.000104-1
- 0.000104 bump

* Mon Mar 05 2018 Petr Pisar <ppisar@redhat.com> - 0.000102-1
- 0.000102 bump

* Wed Feb 14 2018 Petr Pisar <ppisar@redhat.com> - 0.000100-1
- 0.000100 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.000097-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Petr Pisar <ppisar@redhat.com> - 0.000097-1
- 0.000097 bump

* Fri Dec 08 2017 Petr Pisar <ppisar@redhat.com> - 0.000094-2
- Remove unused dependency on Term::ReadKey

* Tue Dec 05 2017 Petr Pisar <ppisar@redhat.com> - 0.000094-1
- 0.000094 bump

* Mon Nov 20 2017 Petr Pisar <ppisar@redhat.com> - 0.000084-1
- 0.000084 bump

* Fri Oct 27 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.000083-1
- 0.000083 bump

* Mon Oct 23 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.000082-1
- 0.000082 bump

* Tue Oct 17 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.000080-1
- 0.000080 bump

* Thu Sep 14 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.000077-1
- 0.000077 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.000072-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Petr Pisar <ppisar@redhat.com> - 0.000072-1
- 0.000072 bump

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.000070-2
- Perl 5.26 rebuild

* Mon Mar 20 2017 Petr Pisar <ppisar@redhat.com> - 0.000070-1
- 0.000070 bump

* Fri Mar 17 2017 Petr Pisar <ppisar@redhat.com> - 0.000069-1
- 0.000069 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.000067-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Petr Pisar <ppisar@redhat.com> - 0.000067-1
- 0.000067 bump

* Tue Dec 20 2016 Petr Pisar <ppisar@redhat.com> - 0.000065-1
- 0.000065 bump

* Mon Dec 19 2016 Petr Pisar <ppisar@redhat.com> - 0.000063-1
- 0.000063 bump

* Thu Sep 29 2016 Petr Pisar <ppisar@redhat.com> - 0.000060-1
- 0.000060 bump

* Fri Sep 02 2016 Petr Pisar <ppisar@redhat.com> - 0.000058-1
- 0.000058 bump

* Mon Aug 01 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.000055-1
- 0.000055 bump

* Fri Jul 29 2016 Petr Pisar <ppisar@redhat.com> - 0.000054-1
- 0.000054 bump

* Tue Jul 19 2016 Petr Pisar <ppisar@redhat.com> - 0.000052-1
- 0.000052 bump

* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 0.000050-1
- 0.000050 bump

* Mon Jul 04 2016 Petr Pisar <ppisar@redhat.com> - 0.000048-1
- 0.000048 bump

* Tue Jun 28 2016 Petr Pisar <ppisar@redhat.com> - 0.000042-1
- 0.000042 bump

* Mon Jun 27 2016 Petr Pisar <ppisar@redhat.com> - 0.000038-1
- 0.000038 bump

* Mon Jun 20 2016 Petr Pisar <ppisar@redhat.com> - 0.000032-1
- 0.000032 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.000030-2
- Perl 5.24 rebuild

* Wed May 11 2016 Petr Pisar <ppisar@redhat.com> - 0.000030-1
- 0.000030 bump

* Mon May 02 2016 Petr Pisar <ppisar@redhat.com> - 0.000029-1
- 0.000029 bump

* Mon Apr 18 2016 Petr Pisar <ppisar@redhat.com> - 0.000028-1
- 0.000028 bump

* Thu Apr 14 2016 Petr Pisar <ppisar@redhat.com> - 0.000027-1
- 0.000027 bump

* Mon Apr 11 2016 Petr Pisar <ppisar@redhat.com> - 0.000026-1
- 0.000026 bump

* Tue Apr 05 2016 Petr Pisar <ppisar@redhat.com> - 0.000025-1
- 0.000025 bump

* Mon Mar 21 2016 Petr Pisar <ppisar@redhat.com> - 0.000024-1
- 0.000024 bump

* Fri Mar 18 2016 Petr Pisar <ppisar@redhat.com> - 0.000023-1
- 0.000023 bump

* Tue Mar 08 2016 Petr Pisar <ppisar@redhat.com> - 0.000022-1
- 0.000022 bump

* Mon Mar 07 2016 Petr Pisar <ppisar@redhat.com> - 0.000021-1
- 0.000021 bump

* Thu Feb 11 2016 Petr Pisar <ppisar@redhat.com> 0.000020-1
- Specfile autogenerated by cpanspec 1.78.
