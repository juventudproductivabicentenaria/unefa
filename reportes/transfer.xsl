<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">

	<xsl:import href="../../../odoo-8.0/openerp/addons/base/report/corporate_defaults.xsl"/>
	<xsl:import href="../../../odoo-8.0/openerp/addons/base/report/rml_template.xsl"/>
	<xsl:variable name="page_format">a4_normal</xsl:variable>

	<xsl:template match="/">
		<xsl:call-template name="rml"/>
	</xsl:template>

	<xsl:template name="stylesheet">
	</xsl:template>

	<xsl:template name="story">
		<xsl:apply-templates select="transfer-list"/>
	</xsl:template>

	<xsl:template match="transfer-list">
		<xsl:apply-templates select="transfer"/>
	</xsl:template>

	<xsl:template match="transfer">
		<setNextTemplate name="other_pages"/>
		<para>
		<b t="1">Document</b>: <i><xsl:value-of select="nombre"/></i>
		</para>
		<setNextTemplate name="first_page"/>
		<pageBreak/>
	</xsl:template>
</xsl:stylesheet>
