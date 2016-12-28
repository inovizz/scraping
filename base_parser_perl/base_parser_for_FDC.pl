#! /usr/bin/perl -w

use Encode qw(encode decode);
use WWW::Mechanize;
use Data::Dumper;

open FILE, "<", $ARGV[0] or die $!;
open OUTFILE, ">", $ARGV[1] or die $!;
binmode OUTFILE;

my %check_url;

while(<FILE>)
{
	my $url = $_;
	chomp($url);
	my $mech = WWW::Mechanize->new(agent => 'Mozilla', autocheck => 0);
	if(!defined $check_url{$url})
	{
		$check_url{$url} = 1;
		$mech->get($url);
		if(! $mech->success)
		{
			print "Failed to load\n";
		}
		my $content = encode('UTF-8',$mech->content());
#print $content;
#exit();
		if(defined $content and $content ne '')
		{
			
			print "$url\n";
			#parse data that you want in output;
			print OUTFILE "----------------------------";
			print OUTFILE "\nURL :: $url";
			#my $url = $mech->{'redirected_uri'};
		
				#title
			if($content =~ m/<title>(.*?)<\//is)
			{
				my $name = $1;
				$name = &trim(&trim_html($name));
				print OUTFILE "\nName1 :: $name" if( $name ne ''); 
			}





			#DOM
			if($content =~ /<td style="width:30%;">(.*?)<\/table>/is)
			{
				my $dom_data = $1;
				@dom_data = split('<\/tr>', $dom_data);
				foreach my $dom_info( @dom_data)
				{
					if($dom_info =~ m/(.*?)<\/b>(.*)/is)
					{
						my $object_name = $1;
						my $object_value = $2;
						$object_value =~ s/<\/li>/, /isg;
						$object_value =~ s/<br \/>/, /isg;
						$object_value =~ s/\s+/ /isg;

						$object_name = &trim(&trim_html($object_name));
						$object_value = &trim(&trim_html($object_value));
						$object_value =~ s/\s*,\s*/, /isg;
						$object_value =~ s/\s*,\s*$//isg;
						$object_value =~ s/\t+/ /isg;
						$object_value =~ s/\s\s+/ /isg;
						$object_name = ucfirst($object_name);
						print OUTFILE "\n$object_name :: $object_value" if( $object_value ne '' or $object_value=~ /!^\s*$/is);
					}
				}
			}
		print OUTFILE "\n";
sleep(3);
		}		
	}
}

close FILE or die $!; 
close OUTFILE or die $!;
 
sub trim
{
	my ($str) = @_;
	$str =~ s/^\s+|\s+$//is if defined $str;
	return($str);
}

sub trim_html
{
	my ($str) =@_;
	$str =~ s/<.*?>//isg if defined $str;
	$str =~ s/&nbsp;//isg if defined $str;
	$str =~ s/\s*<\s*|\s*>\s*//isg if defined $str;
	$str =~ s/^\s+|^\s+$//isg if defined $str;
	return $str;
}
